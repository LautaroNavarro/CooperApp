from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from CooperApp.utils import get_api_launches
# Create your views here.

class Index(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context["api_launches"] = get_api_launches("2018-10-20", "2035-10-20")
        return context
