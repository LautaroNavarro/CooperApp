from django.conf.urls import url
from CooperApp.views import Index

urlpatterns = [
    url(r'^index/', Index.as_view()),
]
