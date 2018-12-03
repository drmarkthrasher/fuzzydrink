from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DrinkForm
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DeleteView)

from .models import Drink

class DrinkListView(LoginRequiredMixin, ListView):
  model = Drink
  #The default template name will be drink_list.html.  This can be changed if desired.
  #Default template variable will be drink_list

  paginate_by = 10


class DrinkDetailView(LoginRequiredMixin, DetailView):
  model = Drink
  template_name = 'consumed/drink_detail.html'

class DrinkCreateView(CreateView):
  form_class = DrinkForm
  model = Drink



class DrinkUpdateView(LoginRequiredMixin, UpdateView):
  # Default html file is drink_form.html.  use command below if want it different
  # template_name = 'consumed/drink_update.html'
  form_class = DrinkForm
  # if using own form, don't declare the fields here!
  # fields = ('drink_type','description','volume','alcohol_content','consumption_time',
  #   'consumption_date', 'favorite' )
  model = Drink
  print("I am just trying to see how the print works!")
  

  def form_valid(self, form):
    form.save()
    return super().form_valid(form)



class DrinkDeleteView(LoginRequiredMixin, DeleteView):
  model = Drink
  success_url = reverse_lazy('drinks')


