from django.shortcuts import render, redirect
from .models import InvListing, Ingredient, Category
from ..login.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    if "id" not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['id'])
    return render(request, 'myfridge/index.html', {"user":user})

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
    messages.info(request, "work in progress")
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
