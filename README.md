# pyt

Pyt is a template engine that uses pure python code. You dont need to learn any new template language to start using it.
There is an example of how to use python code to render templates:


````html

<!-- test.ctp -->
<div>
	<ul>
		<py>
			for item in list:
				<w><li>{{ item.name }}</li></w>
		</py>
	</ul>
</div>
````

And the python code to render the template with a given context:

````python

#coding=utf-8

import test_ctp

test_ctp.render({"list":[{"name":"Item 1"},{"name":"Item 2"}]})

````