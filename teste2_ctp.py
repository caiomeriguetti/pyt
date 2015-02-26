#coding=utf-8
     
from pyt import write
def render(context):
    buffer=""
    
    buffer=write("""
    
    <body>
    	
    """,buffer)
    	
    for user in context["users"]:
    
    	buffer=write(""" """+str(user["nome"])+"""""",buffer)
    	
    buffer=write("""
    
    	
    </body>""",buffer)
    return buffer