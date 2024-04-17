import secrets, json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout,authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.html import escape  
from .models import Chat_Data, UserProfile
from .forms import ProfilePictureForm
from django.views.decorators.csrf import csrf_exempt


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
            response = redirect('homepage')
            response.set_cookie('auth_token', token, httponly=True)
            return response

def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = data.get('user')
        message = escape(data.get('message'))
        Chat_Data.objects.create(user=user, message=message)
        return JsonResponse({'status': 'success'})
    else:
        return render(request, "chat.html")

def chat_messages(request):
    messages = Chat_Data.objects.all().values('user', 'message')
    return JsonResponse(list(messages), safe=False)

def profile_view(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

def game_view(request):
    return render(request, 'game.html')

def upload_profile_picture(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            user_profile.profile_picture = form.cleaned_data['profile_picture']
            user_profile.save()
            return JsonResponse({'message': 'Profile picture uploaded successfully'})
        else:
            return JsonResponse({'error': 'Invalid form data'}, status=400)
    else:
        return JsonResponse({'error': 'Not a valid POST request'}, status=400)