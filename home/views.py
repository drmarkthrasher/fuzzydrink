from django.shortcuts import render
from django.views.generic import View, TemplateView

from consumed.models import Drink

class Home(TemplateView):
  template_name = 'home/index.html'

  def get_context_data(self, **kwargs):
    context = super(Home, self).get_context_data(**kwargs)
    context['num_drinks'] = Drink.objects.all().count()
    return context


