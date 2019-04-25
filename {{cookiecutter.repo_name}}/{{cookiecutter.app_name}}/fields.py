# -*- coding: utf-8 -*-
{% if cookiecutter.fields != "Comma-separated list of fields" %}
from wagtail.core.fields import StreamField

{% for field in cookiecutter.fields.split(',') %}
class {{ block.strip() }}(StreamField):
	pass
    
{% endfor %}
{% endif %}
