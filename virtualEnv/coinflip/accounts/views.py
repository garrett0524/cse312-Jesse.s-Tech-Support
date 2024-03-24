from django.shortcuts import render, redirect
from .database import Database

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        db = Database()
        db.add_login(username, password)
        
        return redirect('login')
    
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        db = Database()
        if db.valid_login(username, password):
            # Perform login logic, e.g., set session, redirect, etc.
            return redirect('home')
        else:
            # Handle invalid login, e.g., display an error message
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')