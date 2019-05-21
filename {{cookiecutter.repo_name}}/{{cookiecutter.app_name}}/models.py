# -*- coding: utf-8 -*-
{% if cookiecutter.pages != "Comma-separated list of custom Wagtail pages" %}
from wagtail.core.models import Page

{% for page in cookiecutter.pages.split(',') %}
class {{ page.strip() }}(Page):
    pass

{% endfor -%}
{% endif %}