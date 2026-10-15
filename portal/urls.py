from django.urls import path
from portal import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index/', views.index),
    path('cadastro/', views.cadastro),
]
