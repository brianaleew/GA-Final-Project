from django.shortcuts import render
from .models import Apparel, Outfit 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def home(request):
    return render(request, 'home.html')


# APPAREL VIEWS
def apparels_index(request):
    apparels = Apparel.objects.all()

    return render(request, 'apparels/index.html', { 'apparels': apparels})

def apparels_detail(request, apparel_id):
    apparel = Apparel.objects.get(id=apparel_id)

    return render(request, 'apparels/detail.html', { 'apparel': apparel })


class ApparelCreate(CreateView):
    model = Apparel
    fields = ['name', 'brand', 'color', 'size', 'img', 'style', 'type']

class ApparelUpdate(UpdateView):
    model = Apparel
    fields = ['name', 'brand', 'color', 'size', 'img', 'style']

class ApparelDelete(DeleteView):
    model = Apparel
    success_url = '/apparels/'


#OUTFIT VIEWS

# this index represents the inspo page (all user outfits will be here)
def outfits_index(request):
    outfits = Outfit.objects.all()

    return render(request, 'outfits/index.html', { 'outfits': outfits})

