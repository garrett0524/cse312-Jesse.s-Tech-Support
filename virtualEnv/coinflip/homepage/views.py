import secrets, json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout,authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.html import escape  
from .models import AuthToken, Chat_Data

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


def like_message(request, message_id):
    if request.method == 'POST':
        message = get_object_or_404(Chat_Data, id=message_id)
        user = request.user

        if user.is_authenticated:
            if user in message.likes.all():
                message.likes.remove(user)
                return JsonResponse({'success': True, 'action': 'unliked'})
            else:
                message.likes.add(user)
                return JsonResponse({'success': True, 'action': 'liked'})
        else:
            return JsonResponse({'success': False, 'error': 'User not authenticated'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
