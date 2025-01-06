from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_form_view, name='user_form'),
    path('success/', views.success_view, name='success'),
]