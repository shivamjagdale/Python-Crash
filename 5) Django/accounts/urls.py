from django.urls import path, include

from . import views

app_name = "accounts"

urlpatterns = [# For all the authentation needs
                path("", include("django.contrib.auth.urls")),

               # For Registration
               path("register/", views.register , name="register") 
               ]

"accounts/register/"