from django.contrib import admin
from django.urls import path ,include
from servicing import views
urlpatterns = [
    path('',views.home ,name="home" ),
    path('delete/',views.deleteredunentdata ,name="delete" ),
    ]