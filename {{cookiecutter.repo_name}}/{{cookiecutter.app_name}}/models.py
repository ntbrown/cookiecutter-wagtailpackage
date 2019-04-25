# -*- coding: utf-8 -*-
{% if cookiecutter.models != "Comma-separated list of models" %}
from django.db import models

from wagtail.core.models import Page

{% for model in cookiecutter.models.split(',') %}
class {{ model.strip() }}(Page):
	pass
    
{% endfor %}
{% endif %}
