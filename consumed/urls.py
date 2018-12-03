from django.urls import path

from . import views


urlpatterns = [
  path('drinks/', views.DrinkListView.as_view(), name='drinks'),
  path('drink/<int:pk>', views.DrinkDetailView.as_view(), name='drink-detail'),
  path('create/', views.DrinkCreateView.as_view(), name='create'),
  path('update/<int:pk>', views.DrinkUpdateView.as_view(), name='update'),
  path('delete/<int:pk>', views.DrinkDeleteView.as_view(), name='delete'),
]