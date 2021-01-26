from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
        url('notice-1/', TemplateView.as_view(template_name="notice/notice_1.html")),
        ]

