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
    path('outfits/<int:outfit_id>/', views.outfits_detail, name='outfits_detail'),
    path('outfits/create/', views.OutfitCreate.as_view(), name='outfits_create'),
    path('outfits/<int:pk>/update/', views.OutfitUpdate.as_view(), name='outfits_update'),
    path('outfits/<int:pk>/delete/', views.OutfitDelete.as_view(), name='outfits_delete'),
    # association links
    path('outfits/<int:outfit_id>/assoc_apparel/<int:apparel_id>/', views.assoc_apparel, name='assoc_apparel'),
    path('outfits/<int:outfit_id>/unassoc_apparel/<int:apparel_id>/', views.unassoc_apparel, name='unassoc_apparel'),
    # user links 
    # signup 
    # log in
    # profile page (going to need edit) --> brings us to recommendations as well(monday task)



    
]