from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/call_click', views.call_click),
    path('register/', views.register, name='register'),
]
