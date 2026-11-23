"""All the urls for accounts related stuff."""

from django.urls import path, include

app_name = "accounts"

urlpatterns = [
                # Default auth urls 
                # Here login url is implemented automatically 
                # But we still need to create login template
                path("", include('django.contrib.auth.urls')),
                ]