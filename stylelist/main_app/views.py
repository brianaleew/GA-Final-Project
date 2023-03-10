from django.shortcuts import render, redirect
from .models import Apparel, Outfit 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(request):
    return render(request, 'home.html')


# APPAREL VIEWS
# display all apparels 
def apparels_index(request):
    apparels = Apparel.objects.all()

    return render(request, 'apparels/index.html', { 'apparels': apparels})
# display one apparel item
def apparels_detail(request, apparel_id):
    apparel = Apparel.objects.get(id=apparel_id)

    return render(request, 'apparels/detail.html', { 'apparel': apparel })


class ApparelCreate(CreateView):
    model = Apparel
    fields = ['name', 'brand', 'color', 'size', 'img', 'style', 'type']

# apparels can update everything except the type field
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

# GOING TO NEED A USER INDEX OF OUTFITS HERE AFTER USER MODEL IS CREATED!!

# view one outfit 
def outfits_detail(request, outfit_id):
    outfit = Outfit.objects.get(id=outfit_id)

    id_list = outfit.apparels.all().values_list('id')

    unused_apparels = Apparel.objects.exclude(id__in=id_list)

    return render(request, 'outfits/detail.html', {'outfit': outfit, 'apparels': unused_apparels })

class OutfitCreate(CreateView):
    model = Outfit
    fields = ['name', 'date', 'event', 'caption']

    def form_valid(self, form):
    # self.request.user is assigning the user
        form.instance.user = self.request.user  
        return super().form_valid(form)

class OutfitUpdate(UpdateView):
    model = Outfit
    fields = ['name', 'date', 'event', 'caption']

class OutfitDelete(DeleteView):
    model = Outfit
    success_url = '/outfits/'

# the assoc apparel func will handle when apparels are added to an outfit
def assoc_apparel(request, outfit_id, apparel_id):
    Outfit.objects.get(id=outfit_id).apparels.add(apparel_id)
    return redirect('outfits_detail', outfit_id=outfit_id)

# the unassoc apparel func will handle removing apparels from an outfit 
def unassoc_apparel(request, outfit_id, apparel_id):
    Outfit.objects.get(id=outfit_id).apparels.remove(apparel_id)
    return redirect('outfits_detail', outfit_id=outfit_id)

# sign up 
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)