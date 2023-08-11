# storeapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('department/<str:department>/', views.department_wikipedia, name='department_wikipedia'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/form/', views.form_view, name='form'),
]
