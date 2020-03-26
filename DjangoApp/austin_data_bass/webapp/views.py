from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. These are called from urls.py.
# A URL will essentially request a certain "view". Process
# and display that view here. 
def home(request):
    return render(request, 'webapp/index.html')

def about(request):
    return render(request, 'webapp/about.html')

def concerts(request):
    return render(request, 'webapp/concerts/index.html')

def artists(request):
    return render(request, 'webapp/artists/index.html')

def venues(request):
    return render(request, 'webapp/venues/index.html')  