from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/call_click', views.call_click),
    path('api/update_boost/', views.update_boost),
    path('register/', views.register, name='register'),
    path('api/update_coins/', views.update_coins),
]
