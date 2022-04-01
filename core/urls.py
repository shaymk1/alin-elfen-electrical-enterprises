
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# app_name = "app"

urlpatterns = [
    
    #if honeypot is installed:
    # path('admin/', include("admin_honeypot.urls", namespces = "admin_honeypot")),
    path('admin/', admin.site.urls),
    path('', include("app.urls")),
    path('about/', include("app.urls")),
    path('services/', include("app.urls")),
    path('contact/', include("app.urls")),
   

  

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
