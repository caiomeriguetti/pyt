#coding=utf-8
import hashlib
import json

def md5(thestr):
    
    h = hashlib.new('md5')
    h.update(thestr)

    return str(h.hexdigest())

def write(s,buffer):
    return buffer+s

def build():
    f=open('config.json')
    
    contents=f.read()
    configdata=json.loads(contents)
    
    for filename in configdata:
        compile(filename)
    
    
def compile(file):
    
    f = open(file)
    
    compiled_content="""#coding=utf-8
     
from pyt import write
def render(context):
    buffer=""
    
    buffer=write(\"\"\"
    
    """
    content=f.read()
    content=content.replace('\n', '\n    ')
    content=content.replace('<w>', 'buffer=write("""')
    content=content.replace('</w>', '""",buffer)')
    content=content.replace('<py>', '""",buffer)')
    content=content.replace('</py>', 'buffer=write("""')
    content=content.replace('<%= ', '"""+str(')
    content=content.replace(' %>', ')+"""')
    content = content+'""",buffer)'
    
    compiled_content = compiled_content + content
    
    
    compiled_content=compiled_content+"""
    return buffer"""
    
    newname=file.replace('.','_')
    
    f2 = open(newname+".py",'w+')
    f2.write(compiled_content)
    f2.close()
    f.close()
