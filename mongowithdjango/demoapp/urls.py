from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,name='happyhome'),
    path('submit/',views.submit,name = 'sub'),
    path('histry/',views.histry,name = 'histry'),
]
