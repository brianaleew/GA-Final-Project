from django.shortcuts import render
from .models import Apparel, Outfit 
# Create your views here.

def home(request):
    return render(request, 'home.html')

def apparels_index(request):
    apparels = Apparel.objects.all()

    return render(request, 'apparels/index.html', { 'apparels': apparels})
