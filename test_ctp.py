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
    
    """)
    extend('lay.ctp')
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
    return buffer