<py>
extend('lay.ctp')

block("conteudo")
</py>

	<body>

<py>

import datetime

for a in [1,2,3]:
	<w><a href='{{ datetime.datetime.now() }}'></a></w>
	
	for b in [4,5,6]:
		<w> 
			Teste {{ b }}
			<br/>
			<br/>
		</w>
	
</py>
	
	<ul>
	
<py>
for a in context["itens"]:
	<w>
		<a>{{ a['nome'] }}</a>
	</w>
</py>
	
	</ul>
	
	<div>
		
		<div>
			
			<div>
				
				<ul>
					<li>
						<div>
<py>

for i in range(1,10):
	<w>
	<a href='{{ i }}' >{{ i }}</a>
	</w>

</py>
						</div>
						
						
					</li>
					
					
					
					
					
				</ul>
				
<py>
element("teste2.ctp",context)
</py>

				
			</div>
			
		</div>
		
	</div>
	
		
	</body>
<py>
endblock()
</py>
