from django.contrib import admin
from .models import Services


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'svg_file')



admin.site.register(Services, ServicesAdmin)

