from django.conf.urls import url
from CooperApp.views import Index, LandingPage

urlpatterns = [
    url(r'^index/', Index.as_view(), name="index"),
    url(r'^', LandingPage, name='landing'),
]
