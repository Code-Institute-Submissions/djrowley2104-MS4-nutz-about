from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index', views.index, name='index')
]


urlpatterns = [
    path('', views.index, name='home'),
    path('mainsite', views.mainsite, name='mainsite')
]