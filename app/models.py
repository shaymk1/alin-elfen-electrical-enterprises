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


