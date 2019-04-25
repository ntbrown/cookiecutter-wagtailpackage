# -*- coding: utf-8 -*-
from django.conf.urls import url


app_name = '{{ cookiecutter.app_name }}'
urlpatterns = [
    {% if cookiecutter.models == "Comma-separated list of models" -%}
    url(r'', TemplateView.as_view(template_name="base.html")),
    {% else -%}
    {% endif -%}
]
