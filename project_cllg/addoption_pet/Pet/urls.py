from .models import Pet
from . import views
from django.urls import path
from .views import PetCreateView,PetUpdateView, PetDeleteView

urlpatterns = [
    
    path('pet_home/',views.Pet_Home, name='pet_home'),
    path('pet_home_dog/',views.Pet_Home_dog, name='pet_home_dog'),
    path('pet_home_cat/',views.Pet_Home_cat, name='pet_home_cat'),
    path('search/',views.search, name='pet_search'),
    path('pet_interested/<int:pk>',views.Interested, name='pet_interested'),
    path('pet/<int:pk>/update', PetUpdateView.as_view(), name='pet_update'),
    path('pet/<int:pk>/delete', PetDeleteView.as_view(), name='pet_delete'),
]


