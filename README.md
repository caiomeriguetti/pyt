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

The **py** tag is where you put the python code. 

There is a limitation with the **py** tag: It must be at the begining of the line( without any spaces ) and the conde inside the tag must follow the identation rules of python

We also have the **w** tag( or write tag ) that is used to write html code when you are inside a **py** tag. In the example, the **w** tag is used to render the **ul** childs.

You are free to use all the python power inside a **py** tag.
