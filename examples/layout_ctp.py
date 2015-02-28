#coding=utf-8
from pyt import Template
class CompiledTemplate(Template):
    def render(self,context=None,blocksdict=None):
        
        if not(context): context={}
        
        if blocksdict:
            self.blocks=blocksdict 
         
        self.currentcontext=context 
        self.write("""
        <html>
    	<head>
    		<title></title>
    	</head>
    	
    	<body>
    
    """)
    	self.fetch("content")
        self.write("""	
    		
    	</body>
    	
    </html>""")
        
        if self.parenttemplate:
            self.element(self.parenttemplate,self.currentcontext,self.blocks)
        
        return self.buffer
def render(context=None,blocksdict=None):
    return CompiledTemplate().render(context,blocksdict)

