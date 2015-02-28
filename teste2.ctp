<py>
extend("lay.ctp")

block('conteudo')

for user in context["users"]:

	<w> {{ user["nome"] }}</w>

endblock()
</py>
