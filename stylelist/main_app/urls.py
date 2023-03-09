from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('apparels/', views.apparels_index, name='apparels_index'),
    path('apparels/<int:apparel_id>/', views.apparels_detail, name='detail'),
    path('apparels/create/', views.ApparelCreate.as_view(), name='apparels_create'),
    path('apparels/<int:pk>/update/', views.ApparelUpdate.as_view(), name='apparels_update'),
    path('apparels/<int:pk>/delete/', views.ApparelDelete.as_view(), name='apparels_delete'),
    # Outfit urls 
    path('outfits/', views.outfits_index, name='outfits_index'),

    
]