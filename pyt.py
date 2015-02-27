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
        

def compile(file):
    
    f = open(file)
    
    compiled_content="""#coding=utf-8

buffer=""

def write(s):
    global buffer
    buffer=buffer+s

def element(name,context):
    name = name.replace('.','_')
    module = __import__(name)
    
    write(module.render(context))
    
def render(context):
    
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
    return buffer"""
    
    newname=file.replace('.','_')
    
    f2 = open(newname+".py",'w+')
    f2.write(compiled_content)
    f2.close()
    f.close()
