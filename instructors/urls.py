from django.urls import path
from instructors import views
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
        url('Ven.Yalagamuwe-Dhammissara-Anunayaka-Thero/', TemplateView.as_view(template_name="instructors/anunayaka_thero.html")),
        url('Dr.Bhanthe-Bokanoruwe-Devananda-Thero/', TemplateView.as_view(template_name="instructors/devananda_thero.html")),
        url('Dr.Bhanthe-Kardetiyana-Gunaratana-Thero/', TemplateView.as_view(template_name="instructors/gunaratana_thero.html")),
        url('Rev-Makulelle-Sugathananda-Thero/', TemplateView.as_view(template_name="instructors/sugathananda_thero.html")),
        url('Ven.Paranagama-Seewaleedhamma-Thero/', TemplateView.as_view(template_name="instructors/seewaleedhamma_thero.html")),
        url('Dr.Liyanage-Dona-Shyamini-Dilrukshi/', TemplateView.as_view(template_name="instructors/dilrukshi.html")),
        ]

