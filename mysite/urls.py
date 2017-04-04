"""mysite URL Configuration

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
from django.conf.urls import include,url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
admin.autodiscover()


urlpatterns = [
#    url(r'^login/$', auth_views.login, name="login"),
#    url(r'^logout/$', auth_views.logout,{"redirect_field_name": "/blog/"} ,name="logout"),
    url(r'^blog/', include('myblog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^imagepool/', include('imagepool.urls')),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^quotes/', include('quote_machine.urls')),
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
