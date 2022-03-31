from django.db import models
from .validators import validate_file_extension

# to accept svg images




class Services(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  svg_file = models.FileField(upload_to="assets/photos",       blank=True,validators = [validate_file_extension])
 

  class Meta:
    verbose_name = 'services'
    verbose_name_plural = 'services'

  def __str__(self):
    return self.title

class About(models.Model):
  header = models.CharField(max_length=200)
  paragraph_1 = models.TextField(blank=True)
  paragraph_2 = models.TextField(blank=True)
  # header_two = models.CharField(max_length=200)
  # description_two = models.TextField(blank=True)
  # header_three = models.CharField(max_length=200)
  # description_three = models.TextField(blank=True)

  class Meta:
    verbose_name = 'about'
    verbose_name_plural = 'about'

  def __str__(self):
    return self.header
    # return f'{self.header_one} {self.header_two} {self.header_three}'


