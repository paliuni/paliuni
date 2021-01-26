from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
        url('material/', TemplateView.as_view(template_name="courseinfo/material.html")),
        url('deploma-in-buddhism/', TemplateView.as_view(template_name="courseinfo/dip_in_buddhism.html")),
        url('BA-1year/', TemplateView.as_view(template_name="courseinfo/ba_1year.html")),
        url('MA-1year/', TemplateView.as_view(template_name="courseinfo/ma_1year.html")),
        url('MA-2year/', TemplateView.as_view(template_name="courseinfo/ma_2year.html")),
        url('M.Phil/', TemplateView.as_view(template_name="courseinfo/mphil.html")),
        url('Ph.D/', TemplateView.as_view(template_name="courseinfo/phd.html")),
        ]

