from django.contrib import admin
from .models import Services, BackgroundImage


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'svg_file')


class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ('bg_image',)


admin.site.register(Services, ServicesAdmin)
admin.site.register(BackgroundImage, BackgroundImageAdmin)
