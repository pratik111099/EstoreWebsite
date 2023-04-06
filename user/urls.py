from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('register/', views.registerView, name='register'),
    path('logout/', views.logoutView, name='logout'),

    path('activate/<uidb64>/<token>', views.activateEmailView, name='activate'),

    path('passwordreset/', views.userPasswordRestView, name='passwordreset'),
    path('passwordresetform/<uidb64>/<token>', views.userPasswordRestViewForm, name='passwordresetform'),
]
