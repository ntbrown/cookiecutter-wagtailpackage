# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.urls import include, re_path, path

urlpatterns = [
    re_path(r'^', include('{{ cookiecutter.app_name }}.urls', namespace='{{ cookiecutter.app_name }}')),
]
