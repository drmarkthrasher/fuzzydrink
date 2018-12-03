from django.forms import ModelForm, Textarea, TimeInput, DateInput
from .models import Drink

class DrinkForm(ModelForm):
  class Meta:
    model = Drink
    fields = "__all__"
    # below is how to specify certain ones in a certain order
    # fields = ['drink_type', 'description','consumption_time']
    # Below is how to override fields
    widgets = {
      # 'description': Textarea(attrs={'cols': 80, 'rows': 1}),
       'consumption_date': DateInput(attrs={}),
       'consumption_time': TimeInput(attrs={}),
    }

  
  



