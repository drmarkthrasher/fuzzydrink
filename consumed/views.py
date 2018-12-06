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

  # typical way to do query if ever needed.
  def get_queryset(self, **kwargs):
    return Drink.objects.all().filter(created_by=self.request.user)
    
  


class DrinkDetailView(LoginRequiredMixin, DetailView):
  model = Drink
  #defaults to drink_detail.html.  Can be changed if desired.
  # template_name = 'consumed/drink_detail.html'
  # default variable in template is drink.  

class DrinkCreateView(LoginRequiredMixin, CreateView):
  form_class = DrinkForm
  model = Drink

  def form_valid(self, form):
    obj = form.save(commit = False)
    obj.created_by = self.request.user
    obj.save()
    return super().form_valid(form)

  def form_invalid(self, form):
    return self.render_to_response(self.get_context_data(form=form))



class DrinkUpdateView(LoginRequiredMixin, UpdateView):
  # Default html file is drink_form.html.  use command below if want it different
  # template_name = 'consumed/drink_update.html'
  form_class = DrinkForm
  # if using own form, don't declare the fields here!
  # fields = ('drink_type','description','volume','alcohol_content','consumption_time',
  #   'consumption_date', 'favorite' )
  model = Drink
  
  def form_valid(self, form):
    form.save()
    return super().form_valid(form)



class DrinkDeleteView(LoginRequiredMixin, DeleteView):
  model = Drink
  success_url = reverse_lazy('drinks')


