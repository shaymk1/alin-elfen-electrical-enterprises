from django.contrib import admin
from .models import Services, About


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'svg_file')


class AboutAdmin(admin.ModelAdmin):
    list_display = ('header', 'paragraph_1', 'paragraph_2')



admin.site.register(Services, ServicesAdmin)
admin.site.register(About, AboutAdmin)

