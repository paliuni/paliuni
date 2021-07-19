from django.urls import path
from instructors import views
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
        url('ven-yalagamuwe-dhammissara-anunayaka-thero/', TemplateView.as_view(template_name="instructors/anunayaka_thero.html")),
        url('dr-bhanthe-bokanoruwe-devananda-thero/', TemplateView.as_view(template_name="instructors/devananda_thero.html")),
        url('dr-bhanthe-kardetiyana-gunaratana-thero/', TemplateView.as_view(template_name="instructors/gunaratana_thero.html")),
        url('rev-makulelle-sugathananda-thero/', TemplateView.as_view(template_name="instructors/sugathananda_thero.html")),
        url('ven-paranagama-seewaleedhamma-thero/', TemplateView.as_view(template_name="instructors/seewaleedhamma_thero.html")),
        url('dr-liyanage-dona-shyamini-dilrukshi/', TemplateView.as_view(template_name="instructors/dilrukshi.html")),
        ]

