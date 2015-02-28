#coding=utf-8
from pyt import Template
class CompiledTemplate(Template):
    def render(self,context=None,blocksdict=None):
        
        if not(context): context={}
        
        if blocksdict:
            self.blocks=blocksdict 
         
        self.currentcontext=context 
        self.write("""
        """)
    	self.extend('examples.layout_ctp')
    
    	self.block("content")
        self.write("""
    
    <h1>Block Example</h1>
    <b>Here you put the block content</b>
    
    """)
    	self.endblock()
        self.write("""""")
        
        if self.parenttemplate:
            self.element(self.parenttemplate,self.currentcontext,self.blocks)
        
        return self.buffer
def render(context=None,blocksdict=None):
    return CompiledTemplate().render(context,blocksdict)

