from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='main'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create')
]
