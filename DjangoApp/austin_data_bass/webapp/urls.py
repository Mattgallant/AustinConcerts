from django.urls import path
from . import views

urlpatterns = [
	#Home, about and search pages
    path('', views.home, name='webapp-home'),
    path('about/', views.about, name='webapp-about'),
    path('search/', views.search, name='webapp-search'),

    #Models
    path('concerts/', views.concerts, name='webapp-concerts'),
    path('concerts/<str:concert_name>/', views.concert_name, name='webapp-concerts-instance'),

    path('venues/', views.venues, name='webapp-venues'),
    path('venues/<str:venue_name>/', views.venue_name, name='webapp-venues-instance'),

    path('artists/', views.artists, name='webapp-artists'),
    path('artists/<str:artist_name>/', views.artist_name, name='webapp-artists-instance'),
    
]
