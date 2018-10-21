from django.conf.urls import url
from CooperApp.views import Index, LandingPage, create_user_of_news

urlpatterns = [
    url(r'^index/', Index.as_view(), name="index"),
    url(r'^save_news/', create_user_of_news, name='save_news'),
    url(r'^', LandingPage, name='landing'),
]
