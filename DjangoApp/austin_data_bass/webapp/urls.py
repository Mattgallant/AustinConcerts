from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='webapp-home'),
    path('about/', views.about, name='webapp-about'),
    path('concerts/', views.concerts, name='webapp-concerts'),
    path('venues/', views.venues, name='webapp-venues'),
    path('venues/<str:venue_name>/', views.venue_name, name='webapp-venues-instance'),

    path('artists/', views.artists, name='webapp-artists'),
    path('artists/<str:artist_name>/', views.artist_name, name='webapp-artists-instance'),

    #Development url... just for messing around
    path('dev/', views.dev, name='webapp-dev'),
]