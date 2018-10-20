from django.conf.urls import url
from CooperApp.views import index

urlpatterns = [
    url(r'^index/', index),
]
