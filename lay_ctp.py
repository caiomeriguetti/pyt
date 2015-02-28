#coding=utf-8

buffer=""
currentcontext=None
parenttemplate=False
currentblock=None
blocks={}

def extend(name):
    global parenttemplate
    buffer=""
    parenttemplate=name
    
def fetch(name):
    global blocks
    
    if blocks and name in blocks.keys(): 
        write(blocks[name])

def block(name):
    global currentblock
    currentblock=name

def endblock():
    global currentblock
    currentblock=None

def write(s):
    global currentblock
    if currentblock:
        global blocks
        if not(currentblock in blocks.keys()):
            blocks[currentblock]=""
        blocks[currentblock]=blocks[currentblock]+s
    else:
        global buffer
        buffer=buffer+s

def element(name,context,blocks=None):
    name = name.replace('.','_')
    module = __import__(name)
    
    write( module.render(context,blocks) )
    
def render(context,blocksdict=None):
    global currentcontext
    global blocks
    
    if blocksdict:
        blocks=blocksdict
     
    currentcontext=context 
    write("""
    
    <html>
    	
    
    """)
    fetch("conteudo")
    write("""
    	
    	
    </html>""")
    
    if parenttemplate:
        element(parenttemplate,currentcontext,blocks)
    
    return buffer