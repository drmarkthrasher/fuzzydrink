from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View, TemplateView
from django.views.generic.edit import FormView

from consumed.models import Drink
from .forms import SignUpForm

class Home(TemplateView):
  template_name = 'home/index.html'

  def get_context_data(self, **kwargs):
    context = super(Home, self).get_context_data(**kwargs)
    context['num_drinks'] = Drink.objects.all().count()
    return context


class Signup(FormView):
  form_class = SignUpForm  # inherited from stock form that comes with django (UserCreationForm)
  template_name = 'home/signup.html'
  

  def form_valid(self, form):
    form.save()
    username = form.cleaned_data.get('username')
    raw_password = form.cleaned_data.get('password1')
    user = authenticate(username=username, password=raw_password)
    login(self.request, user)
    return redirect('home')

  def form_invalid(self, form):
    print("This is invalid")
    return super().form_invalid(form)
    
  
  # def post(self, request, *args, **kwargs):
  #   if request.POST['password1'] == request.POST['password2']:
  #     print('They match')
    
      
  #   return HttpResponseRedirect('home')
    
    
    
    


