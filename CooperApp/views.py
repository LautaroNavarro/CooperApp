from django.shortcuts import render
from django.views.generic.base import TemplateView
from CooperApp.utils import get_api_launches
from CooperApp.models import *
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
# Create your views here.


def LandingPage(request):
    return render(request, 'landing.html')


class Index(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        if self.request.GET.get('start_date') and self.request.GET.get('end_date'):
        	start_date = self.request.GET.get('start_date')
        	end_date = self.request.GET.get('end_date')
        else:
        	start_date = ""
        	end_date = ""
        context["api_launches"] = get_api_launches(start_date, end_date)
        return context


def create_user_of_news(request):
	email = request.POST.get("email")
	NewsLetterSubscribed.objects.create(email=email)
	return redirect(reverse('index'))