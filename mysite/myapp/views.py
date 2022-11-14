from django.shortcuts import render
from .models import Consume, Food
from django.contrib.auth.models import User
# Create your views here.

def index(request):

    if request.method == "POST":
        food_consumed = request.POST['food_consumed'] #name alone, from the form
        consume = Food.objects.get(name=food_consumed) # gets the object that matches the name "food_consumed"
        #get current user:
        user = request.user
        #construct object of type Consume:
        consume = Consume(user = user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()


    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user) #fetches all consumed items
    return render(request, "myapp/index.html",{"foods":foods, 'consumed_food':consumed_food})
