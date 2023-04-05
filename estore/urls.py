from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepageView, name='home'),
]
