from django.contrib import admin
from .models import Apparel, Outfit

# Register your models here.
admin.site(Apparel)

admin.site(Outfit)
