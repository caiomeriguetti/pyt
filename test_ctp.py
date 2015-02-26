#coding=utf-8
     
from pyt import write
def render(context):
    buffer=""
    
    buffer=write("""
    
    <body>
    	
    
    	
    
    """,buffer)
    
    import datetime
    
    for a in [1,2,3]:
    	buffer=write("""<a href='"""+str(datetime.datetime.now())+"""'></a>""",buffer)
    	
    	for b in [4,5,6]:
    		buffer=write(""" 
    			Teste """+str(b)+"""
    			<br/>
    			<br/>
    		""",buffer)
    	
    buffer=write("""
    
    <ul>
    
    """,buffer)
    for a in context["itens"]:
    	buffer=write("""
    		<a>"""+str(a['nome'])+"""</a>
    	""",buffer)
    buffer=write("""
    
    </ul>
    
    <div>
    	
    	<div>
    		
    		<div>
    			
    			<ul>
    				<li>
    					<div>
    """,buffer)
    
    for i in range(1,10):
    	buffer=write("""
    	<a href='"""+str(i)+"""' >"""+str(i)+"""</a>
    	""",buffer)
    
    buffer=write("""
    						
    						
    					</div>
    					
    					
    				</li>
    				
    				
    			</ul>
    			
    			
    		</div>
    		
    	</div>
    	
    </div>
    
    	
    </body>""",buffer)
    return buffer