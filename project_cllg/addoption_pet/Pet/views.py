from django.core import paginator
from django.shortcuts import render,redirect,get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Pet
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
context = {'pets':Pet.objects.all()}
    
    
def Interested(request,pk):
    pet = get_list_or_404(Pet, id =request.POST.get('pet_id'))
    print(pet)
    print(pet.pet_interest)
    pet.pet_interest.add(request.user)
    return HttpResponseRedirect(reverse('pet_detail',args=[str(pk)]))


class PetCreateView(LoginRequiredMixin,CreateView):
    model= Pet
    fields = ['pet_name','pet_category','pet_age','pet_bread','pet_gender','pet_image','pet_vaccinated','pet_neutered','pet_sprayed','pet_good_kids','pet_address']
    def form_valid(self, form) :
     print('check')
     print(Pet.pet_owner)
     print(self.request.user)
     form.instance.pet_owner=self.request.user  
     return super().form_valid(form)

class PetDetailView(DetailView):
    model = Pet
    template_name='Pet/pet_detail.html'
    
class PetUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):    
    model= Pet
    pet = Pet.pet_owner
    print(pet)
    fields = ['pet_name','pet_category','pet_age','pet_bread','pet_gender','pet_image','pet_vaccinated','pet_neutered','pet_sprayed','pet_good_kids','pet_address']
    def form_valid(self, form) :
        print('check')
        print(form.instance.owner)
        print(self.request.user)
        form.instance.owner=self.request.user
        return super().form_valid(form)

    def test_func(self):
        pet=self.get_object()
        print(self.get_object())
        print("check")
        print(self.request.user)
        if self.request.user == pet.pet_owner:
            return True
        return False    

class PetDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Pet
    success_url = '/pet_home'
    def test_func(self):
        pet=self.get_object()
        print(self.get_object())
        print("check")
        print(self.request.user)
        if self.request.user == pet.pet_owner:
            return True
        return False
    
@login_required
def Pet_Home(request):
    context = Pet.objects.all()
    paginator = Paginator(context,9)
    page_num= request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request,'Pet/pet_home.html',{'pets':page_obj})

@login_required
def Pet_Home_dog(request):
    return render(request,'Pet/pet_dog.html',context)

@login_required
def Pet_Home_cat(request):
    return render(request,'Pet/pet_cat.html',context)

@login_required
def search(request):
    return render(request,'Pet/pet_search.html')