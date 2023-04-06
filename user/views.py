from django.shortcuts import render, redirect
from .forms import loginForm, registrationForm
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginView(request):
    form = loginForm()

    if request.method == "POST":
        

        email = request.POST.get('email')
        password = request.POST.get('password')
    
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'user does not exit')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You login Successfully')
            return redirect('home')
        
        else:
            messages.error(request,'Credentials does not match')
    context = {
        'name' : 'login',
        'form' : form
    }
    return render(request, 'user/login.html', context)

def logoutView(request):
    logout(request)
    messages.success(request, 'You logout Successfully')
    return redirect('home')

def registerView(request):
    if request.method == "POST":
        form = registrationForm(request.POST)
        
        # user = form.save(commit=False)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = new_user.email
            print(new_user.username)
            new_user.save()
            return redirect('login')

    else:
        form = registrationForm()

    context = {
        'form': form,
    }
    return render(request, 'user/login.html', context)
