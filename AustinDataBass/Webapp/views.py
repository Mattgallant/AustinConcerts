from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def splash(request):
	return render(request, 'Webapp/index.html')

def about(request):
	return render(request, 'Webapp/about.html')
