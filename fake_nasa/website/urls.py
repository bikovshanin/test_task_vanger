from django.urls import path

from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('photos/', views.photo_gallery, name='photo_gallery'),
]
