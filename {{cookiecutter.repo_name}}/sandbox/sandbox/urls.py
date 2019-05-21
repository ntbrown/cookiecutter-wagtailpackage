"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import views as wagtail_views
from wagtail.core.urls import WAGTAIL_FRONTEND_LOGIN_TEMPLATE, serve_pattern
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
	path('django-admin/', admin.site.urls),
	path('admin/', include(wagtailadmin_urls)),
	path('docs/', include(wagtaildocs_urls)),
	path('', include('{{ cookiecutter.app_name }}.urls', namespace='{{ cookiecutter.app_name }}')),
	re_path(serve_pattern, wagtail_views.serve, name='wagtail_serve'),
]


if settings.DEBUG:
	from django.conf.urls.static import static
	from django.contrib.staticfiles.urls import staticfiles_urlpatterns

	# Serve static and media files from development server
	urlpatterns += staticfiles_urlpatterns()
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
