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
    
    """)
    extend('lay.ctp')
    
    block("conteudo")
    write("""
    
    	<body>
    
    """)
    
    import datetime
    
    for a in [1,2,3]:
    	write("""<a href='"""+str( datetime.datetime.now() )+"""'></a>""")
    	
    	for b in [4,5,6]:
    		write(""" 
    			Teste """+str( b )+"""
    			<br/>
    			<br/>
    		""")
    	
    write("""
    	
    	<ul>
    	
    """)
    for a in context["itens"]:
    	write("""
    		<a>"""+str( a['nome'] )+"""</a>
    	""")
    write("""
    	
    	</ul>
    	
    	<div>
    		
    		<div>
    			
    			<div>
    				
    				<ul>
    					<li>
    						<div>
    """)
    
    for i in range(1,10):
    	write("""
    	<a href='"""+str( i )+"""' >"""+str( i )+"""</a>
    	""")
    
    write("""
    						</div>
    						
    						
    					</li>
    					
    					
    					
    					
    					
    				</ul>
    				
    """)
    element("teste2.ctp",context)
    write("""
    
    				
    			</div>
    			
    		</div>
    		
    	</div>
    	
    		
    	</body>
    """)
    endblock()
    write("""
    """)
    
    if parenttemplate:
        element(parenttemplate,currentcontext,blocks)
    
    return buffer