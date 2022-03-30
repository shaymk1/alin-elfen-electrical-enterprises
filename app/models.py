from django.db import models

class Services(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(blank=True)
  image = models.ImageField(upload_to='photos')

  def __str__(self):
    return self.name

class BackgroundImage(models.Model):
  bg_image = models.ImageField(upload_to='photos')
