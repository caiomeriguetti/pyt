#coding=utf-8

buffer=""
currentcontext=None
def extend(name):
    buffer=""
    element(name,currentcontext)
    pass

def write(s):
    global buffer
    buffer=buffer+s

def element(name,context):
    name = name.replace('.','_')
    module = __import__(name)
    
    write(module.render(context))
    
def render(context):
    currentcontext=context
    write("""
    
    <html>
    	
    	
    	
    	
    </html>""")
    return buffer