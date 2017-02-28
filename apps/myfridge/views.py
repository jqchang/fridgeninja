from django.shortcuts import render, redirect
from django.db.models import DateTimeField, ExpressionWrapper, F
from django.db import models
from .models import InvListing, Ingredient, Category
from ..login.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    if "id" not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['id'])
    fridge = InvListing.objects.filter(user_id=request.session["id"])
    # .annotate(expires_at=F('created_at') + F('shelflife'), output_field=models.DateTimeField())
    return render(request, 'myfridge/index.html', {"user":user, "fridge":fridge})

def new(request):
    return render(request, 'myfridge/new.html')

def add(request):
    if "id" not in request.session:
        return redirect('/')
    if request.method == 'POST':
        valid_add = InvListing.objects.validate(request.POST, request.session["id"])
    if not valid_add["success"]:
        for msg in valid_add["error_list"]:
            messages.info(request, msg)
    return redirect('/myfridge')

def edit(request, product_id):
    messages.info(request, "work in progress")
    return redirect('/')

def create(request):
    if request.method == 'POST':
        valid_add = Ingredient.objects.validate(request.POST)
    if not valid_add["success"]:
        for msg in valid_add["error_list"]:
            messages.info(request, msg)
    else:
        messages.info(request, "Successfully added ingredient '{}' to database - now add it to your fridge!".format(valid_add["ingred_object"].name))

    return redirect('/')

def read(request, ingr_id):
    messages.info(request, 'work in progress')
    return redirect('/')

def update(request, product_id):
    messages.info(request, 'work in progress')
    return redirect('/')

def destroy(request, product_id):
    messages.info(request, 'work in progress')
    return redirect('/')
