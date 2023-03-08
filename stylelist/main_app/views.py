from django.shortcuts import render
from .models import Apparel, Outfit 
from django.views.generic.edit import CreateView 

# Create your views here.

def home(request):
    return render(request, 'home.html')

def apparels_index(request):
    apparels = Apparel.objects.all()

    return render(request, 'apparels/index.html', { 'apparels': apparels})

def apparels_detail(request, apparel_id):
    apparel = Apparel.objects.get(id=apparel_id)

    return render(request, 'apparels/detail.html', { 'apparel': apparel })

class ApparelCreate(CreateView):
    model = Apparel
    fields = ['name', 'brand', 'color', 'size', 'img', 'style', 'type']



