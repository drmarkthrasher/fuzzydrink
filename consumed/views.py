from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView, ListView, DetailView

from .models import Drink

class DrinkListView(LoginRequiredMixin, ListView):
  model = Drink
  #The default template name will be drink_list.html.  This can be changed if desired.
  #Default template variable will be drink_list.

  paginate_by = 10


class DrinkDetailView(LoginRequiredMixin, DetailView):
  model = Drink
  template_name = 'consumed/drink_detail.html'

