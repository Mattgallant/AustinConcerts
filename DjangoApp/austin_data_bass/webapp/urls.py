from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='webapp-home'),
    path('about/', views.about, name='webapp-about'),
    path('concerts/', views.concerts, name='webapp-concerts'),
    path('venues/', views.venues, name='webapp-venues'),
    path('artists/', views.artists, name='webapp-artists'),
    path('dev/', views.dev, name='webapp-dev'),
]