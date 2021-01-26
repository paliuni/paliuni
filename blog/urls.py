from django.urls import path
from django.conf.urls import url
from blog import views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
        path('', views.blog),
        url(r'^(?P<slug>[\w-]+)/$', views.blog_details, name="detail"),
        url(r'^(?P<slug>[\w-]+)/comment/$', views.comment),
        url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
        ]

