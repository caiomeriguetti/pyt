#coding=utf-8
import hashlib
import json
from bs4 import BeautifulSoup

def md5(thestr):
    
    h = hashlib.new('md5')
    h.update(thestr)

    return str(h.hexdigest())

def build():
    f=open('config.json')
    
    contents=f.read()
    configdata=json.loads(contents)
    
    for filename in configdata:
        compile(filename)
        

class Template():
    
    buffer=""
    currentcontext=None
    parenttemplate=False
    currentblock=None
    blocks={}
    
    def extend(self,name):
        self.buffer=""
        self.parenttemplate=name
    
    def fetch(self,name):
        global blocks
        
        if blocks and name in blocks.keys(): 
            write(blocks[name])
    
    def __init__(self,template_string):
        self.string=template_string
        
    def compile(self):
        

def compile(file):
    
    f = open(file)
    
    compiled_content="""#coding=utf-8

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
    write(\"\"\"
    
    """
    content=f.read()
    content=content.replace('\n', '\n    ')
    content=content.replace('<w>', 'write("""')
    content=content.replace('</w>', '""")')
    content=content.replace('<py>', '""")')
    content=content.replace('</py>', 'write("""')
    content=content.replace('{{', '"""+str(')
    content=content.replace('}}', ')+"""')
    content = content+'""")'
    
    compiled_content = compiled_content + content
    
    
    compiled_content=compiled_content+"""
    
    if parenttemplate:
        element(parenttemplate,currentcontext,blocks)
    
    return buffer"""
    
    newname=file.replace('.','_')
    
    f2 = open(newname+".py",'w+')
    f2.write(compiled_content)
    f2.close()
    f.close()
