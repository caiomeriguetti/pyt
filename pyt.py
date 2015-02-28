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

        if self.blocks and name in self.blocks.keys(): 
            self.write(self.blocks[name])
            
    def block(self,name):
        self.currentblock=name
    
    def endblock(self,):
        self.currentblock=None
    
    def write(self,s):

        if self.currentblock:
            
            if not(self.currentblock in self.blocks.keys()):
                self.blocks[self.currentblock]=""
            
            self.blocks[self.currentblock]=self.blocks[self.currentblock]+s
            
        else:
            self.buffer=self.buffer+s
    
    def element(self,name,context=None,blocks=None):
        
        module = __import__(name,fromlist=[''])
        
        if not(context): context = self.currentcontext
        
        self.write( module.render(context,blocks) )

def compile(file):
    
    f = open(file)
    
    compiled_content="""#coding=utf-8
from pyt import Template
class CompiledTemplate(Template):
    def render(self,context=None,blocksdict=None):
        
        if not(context): context={}
        
        if blocksdict:
            self.blocks=blocksdict 
         
        self.currentcontext=context 
        self.write(\"\"\"
        """
    content=f.read()
    content=content.replace('\n', '\n    ')
    content=content.replace('<w>', 'self.write("""')
    content=content.replace('</w>', '""")')
    content=content.replace('<py>', '""")')
    content=content.replace('</py>', '    self.write("""')
    content=content.replace('{{', '"""+str(')
    content=content.replace('}}', ')+"""')
    content = content+'""")'
    
    compiled_content = compiled_content + content
    
    compiled_content=compiled_content+"""
        
        if self.parenttemplate:
            self.element(self.parenttemplate,self.currentcontext,self.blocks)
        
        return self.buffer
def render(context=None,blocksdict=None):
    return CompiledTemplate().render(context,blocksdict)

"""
        
    newname=file.replace('.','_')
    
    f2 = open(newname+".py",'w+')
    f2.write(compiled_content)
    f2.close()
    f.close()
