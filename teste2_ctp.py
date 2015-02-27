#coding=utf-8

buffer=""

def write(s):
    global buffer
    buffer=buffer+s

def element(name,context):
    name = name.replace('.','_')
    module = __import__(name)
    
    write(module.render(context))
    
def render(context):
    
    write("""
    
    <div>
    	
    """)
    	
    for user in context["users"]:
    
    	write(""" """+str( user["nome"] )+"""""")
    	
    write("""
    
    	
    </div>""")
    return buffer