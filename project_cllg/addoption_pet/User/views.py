from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from .forms import RegisterForm,UserUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate 
# Create your views here.
def User_reg(request):
    # print(request.method)
    # print('check')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # print(form)
        # print('check2')
        if form.is_valid():
            # print('TRUE')
            form.save()
            messages.success(request,'you have account has been created !!you are now able to log in ')
            return redirect('login')
    else:
        print('FALSE')
        form = RegisterForm()
    return render(request,'User/register.html',{'form':form})

def log_in(request):
    print("check")
    if request.method == "POST":
        print("i am in if")
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            print('i am going through my test')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid use or password.")
    form = AuthenticationForm()

    return render(request,'User/templates/login.html',{'form':form})

def log_out(request):
    auth.logout(request)
    return redirect('/index')

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request,f'your account has been updated ')
            return redirect('/')
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'u_form': u_form,
    }
    return render(request,'User/profile.html',context)