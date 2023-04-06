from Estorewebsite import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import loginForm, registrationForm
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import generate_token
from django.core.mail import EmailMessage

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
        
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = new_user.email
            print(new_user.username)
            new_user.is_active = False
            new_user.save()
            messages.success(request, 'You Successfully Created Account. We have send comfirmation email')

            current_site = get_current_site(request)
            subject = 'Welcome to EStore'
            message = render_to_string('user/email-confirmation.html',{
                      'name': new_user.first_name,
                      'domain': current_site.domain,
                      'uid': urlsafe_base64_encode(force_bytes(new_user.id)),
                      'token': generate_token.make_token(new_user)
            })

            email = EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [new_user.email],
            )
            email.fail_silently = True
            email.send()
            return redirect('login')

    else:
        form = registrationForm()

    context = {
        'form': form,
    }
    return render(request, 'user/login.html', context)


def activateEmailView(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(id=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        messages.success(request, 'Your account successfully activated')
        return redirect('login')
    
    else:
        return HttpResponse('Activation failed, Please try again!!!')