# -*- coding: utf-8 -*-
{% if cookiecutter.blocks != "Comma-separated list of blocks" %}
from wagtail.core import blocks

{% for block in cookiecutter.blocks.split(',') %}
class {{ block.strip() }}(blocks.StructBlock):
	pass
    
{% endfor %}
{% endif %}
