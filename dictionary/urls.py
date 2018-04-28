from django.conf.urls import url
from django.views.generic import TemplateView
from dictionary.api import WordApi

urlpatterns = [
    url(r'^word-api$', WordApi.as_view()),
    url(r'^app', TemplateView.as_view(template_name="dictionary/index.html"))
]
