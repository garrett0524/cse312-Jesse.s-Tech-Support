import secrets, json, random, time
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout,authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.html import escape  
from .models import Chat_Data, UserProfile, Player, Game
from .realtime import update_game_list, update_balance, update_free_money_balance
from .forms import ProfilePictureForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


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
    if request.method == 'POST':
        bio = request.POST.get('bio', '')
        user.userprofile.bio = bio[:200]  # Truncate the bio to 200 characters
        user.userprofile.save()
    return render(request, 'profile.html', {'user': user})

def game_view(request):
    return render(request, 'game.html')

def lobby_view(request):
    if request.user.is_authenticated:
        available_games = Game.objects.filter(player2=None, completed=False)
        user_profile = request.user.userprofile
        
        context = {
            'user': request.user,
            'games': available_games,
            'balance': user_profile.currency,
            'wins': user_profile.wins,
            'losses': user_profile.loses,
        }
        
        return render(request, 'lobby.html', context)
    else:
        return redirect('/login')

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
    
def create_game(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            side = request.POST.get('side')
            bet = int(request.POST.get('bet'))
            if bet < 0:
                error_message = "Invalid bet amount."
                return render(request, 'create_game.html', {'error_message': error_message})

            user_profile = request.user.userprofile
            if user_profile.currency >= bet:
                player = Player.objects.create(user_profile=user_profile, side=side)
                Game.objects.create(player1=player, bet=bet)
                user_profile.currency -= bet
                user_profile.save()
                
                # Get the updated game list data
                game_list_data = Game.objects.filter(completed=False).values()
                
                # Trigger the real-time update for the game list
                update_game_list(game_list_data)
                
                return redirect('/lobby')
            else:
                error_message = "Insufficient balance to create the game."
                return render(request, 'create_game.html', {'error_message': error_message})
        else:
            return redirect('/login')
    else:
        return render(request, 'create_game.html')

def game_list(request):
    if request.user.is_authenticated:
        available_games = Game.objects.filter(player2=None, completed=False)
        user_profile = request.user.userprofile
        
        context = {
            'user': request.user,
            'games': available_games,
            'balance': user_profile.currency,
            'wins': user_profile.wins,
            'losses': user_profile.loses,
        }
        
        return render(request, 'game_list.html', context)
    else:
        return redirect('/login')
    
def play_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            if game.player1.user_profile.user != request.user and not game.completed:
                user_profile = request.user.userprofile
                if game.player1.side == 'heads':
                    player2_side = 'tails'
                else:
                    player2_side = 'heads'
                player2 = Player.objects.create(user_profile=user_profile, side=player2_side)
                game.player2 = player2
                game.save()
                winning_side = random.choice(['heads', 'tails'])
                if winning_side == game.player2.side:
                    game.player2.user_profile.currency += game.bet
                    game.player2.user_profile.wins += 1
                    game.player1.user_profile.loses += 1
                    result = 'win'
                else:
                    game.player1.user_profile.currency += game.bet * 2
                    game.player2.user_profile.currency -= game.bet
                    game.player1.user_profile.wins += 1
                    game.player2.user_profile.loses += 1
                    result = 'lose'
                game.player1.user_profile.save()
                game.player2.user_profile.save()
                game.completed = True
                game.save()
                # Get the updated balance data for both players
                player1_balance = game.player1.user_profile.currency
                player2_balance = game.player2.user_profile.currency
                # Trigger the real-time update for the balances
                update_balance(game.player1.user_profile.user.id, player1_balance)
                update_balance(game.player2.user_profile.user.id, player2_balance)
                # Get the updated game list data
                game_list_data = Game.objects.filter(completed=False).values()
                # Trigger the real-time update for the game list
                update_game_list(game_list_data)
                return render(request, 'play_game.html', {'game': game, 'result': result})
            else:
                return render(request, 'play_game.html', {'game': game})
        else:
            return redirect('/login')
    else:
        return render(request, 'play_game.html', {'game': game})
    
def get_user_data(request):
    if request.user.is_authenticated:
        user_profile = request.user.userprofile
        data = {
            'balance': user_profile.currency,
            'wins': user_profile.wins,
            'losses': user_profile.loses,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

def get_player_username(request, player1_id):
    player = Player.objects.get(id=player1_id)
    username = player.user_profile.user.username
    return JsonResponse({'username': username})

def free_money(request):
    if request.user.is_authenticated:
        user_profile = request.user.userprofile
        
        if request.method == 'POST':
            last_claim_time = request.session.get('last_claim_time', 0)
            current_time = time.time()
            
            if current_time - last_claim_time >= 5:  # Check if 5 seconds have passed since the last claim
                user_profile.currency += 10000
                user_profile.save()
                request.session['last_claim_time'] = current_time
                
                # Trigger the real-time update for the balance
                update_free_money_balance(request.user.id, user_profile.currency)
                
                return JsonResponse({'success': True, 'message': 'You have earned $10,000!', 'cooldown': 5})
            else:
                remaining_time = int(5 - (current_time - last_claim_time))
                return JsonResponse({'success': False, 'message': f'Please wait {remaining_time} seconds before claiming again.', 'cooldown': remaining_time})
        
        return render(request, 'free_money.html')
    else:
        return redirect('/login')

def user_profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return render(request, 'user_profile.html', {'error': 'User does not exist'})

    return render(request, 'user_profile.html', {'user': user})