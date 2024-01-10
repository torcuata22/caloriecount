from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Consume, Food
from .forms import SignUpForm
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='/login')  
def index(request):
    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)

        # Use request.user directly after ensuring the user is authenticated
        user = request.user

        consume_entry = Consume(user=user, food_consumed=consume)
        consume_entry.save()

        foods = Food.objects.all()
    else:
        foods = Food.objects.all()

    if request.user.is_authenticated:
        user_id = request.user.id
        consumed_food = Consume.objects.filter(user_id=user_id)
    else:
        consumed_food = None  # Set to None or handle accordingly for non-authenticated users
    
    return render(request, "myapp/index.html", {"foods": foods, 'consumed_food': consumed_food})


def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == "POST":
        consumed_food.delete()
        return redirect ('/')
    return render(request, 'myapp/delete.html')

def delete_all(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    
    current_date = timezone.now().date()
    Consume.objects.filter(user = request.user).delete()
    messages.success(request, "All entries for today have been deleted.")
    
    return redirect('index')

#AUTHENTICATION:

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to your index page
    else:
        form = SignUpForm()

    return render(request, 'myapp/signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) #calls djangon authentication system
        if user is not None:
            login(request, user)
            messages.success(request, ("Login successful!"))
            return redirect('index')
        else:
            messages.success(request, ("Oops, something went wrong. Please try again"))
            return redirect('login_user')
    else:    
        return render(request, 'myapp/login.html', {})

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, ("You have logged out successfully"))
    return redirect('login')