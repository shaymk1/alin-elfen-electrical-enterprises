from django.contrib import admin
from .models import *


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'svg_file')


class AboutAdmin(admin.ModelAdmin):
    list_display = ('header', 'paragraph_1', 'paragraph_2')


admin.site.register(Services, ServicesAdmin)
admin.site.register(About, AboutAdmin)


# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'email', 'message')
#     list_display_links = ('first_name', 'email', 'message')
#     list_filter = ('email',)


# admin.site.register(Contact, ContactAdmin)

