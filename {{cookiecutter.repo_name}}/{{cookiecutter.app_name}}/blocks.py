# -*- coding: utf-8 -*-
from wagtail.core import blocks

{% for block in cookiecutter.blocks.split(',') %}
class {{ block.strip() }}(blocks.StructBlock):
	pass
    
{% endfor %}
{% endif %}
