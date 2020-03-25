from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='page-splash'),    	#Home/Splash Page
    path('about/', views.about, name='page-about'), #About page

    #Model home pages
    #path('venues/', views.about, name='page-venues'), 
   # path('concerts/', views.about, name='page-artists'),   
   # path('artists/', views.about, name='page-artists'),  
]