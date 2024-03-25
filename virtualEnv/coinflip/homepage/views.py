import secrets
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import logout,authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import AuthToken

def homepage(request):
    return render(request, "starterHTML.html", {'user': request.user})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('homepage')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token = secrets.token_hex(32)
            AuthToken.objects.create(user=user, token=token)
            response = redirect('homepage')
            response.set_cookie('auth_token', token, httponly=True)
            return response

def chat(request):
    template = loader.get_template("chat.html")
    return HttpResponse(template.render())


