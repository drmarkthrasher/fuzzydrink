from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Drink(models.Model):
  DRINK_TYPE = (
    ('b', 'Beer'),
    ('w', 'Wine'),
    ('s', 'Shot'),
    ('c', 'Cocktail')
  )

  drink_type = models.CharField(
    max_length=1,
    choices=DRINK_TYPE,
    default='b'
  )
  description = models.CharField(max_length=255)
  volume = models.DecimalField(default=0, decimal_places=1, max_digits=4, 
    help_text = "Ounces of drink")
  alcohol_content = models.DecimalField(default=0, decimal_places=1, max_digits=4,
    help_text="This is half the proof")
  consumption_date = models.DateField()
  consumption_time = models.TimeField()
  favorite = models.BooleanField(default=False)

  class	Meta:
    ordering=['consumption_date', 'consumption_time']
    #Note, put "-" in front of field to reverse sort.  i.e., '-consumption_date'

  def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        # return reverse('drink-detail', args=[str(self.id)])
        return reverse('drink-detail', kwargs={'pk': self.pk})

  def get_update_url(self):
        return reverse('update', kwargs={'pk': self.pk})

  def	get_delete_url(self):
        return reverse('delete', kwargs={'pk': self.pk})

  def __str__(self):
    return self.description


