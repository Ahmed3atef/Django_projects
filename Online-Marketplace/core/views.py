from django.shortcuts import render, redirect
from item.models import Category, Item
from django.contrib.auth import views as auth_views
from core.forms import LoginForm
from django.contrib.auth import logout
from core import forms

def index(request):
    # get all items that is not sold get first 6 items
    items = Item.objects.filter(is_sold = False)[0:6]
    categories = Category.objects.all()
    return render(request, "core/index.html", {
        'categories':categories,
        'items':items
    })

def contact(request):
    return render(request, "core/content.html")


def signup(request):
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/login/')
        
    form = forms.SignupForm()
    
    return render(request, 'core/signup.html',{
        'form':form
    })

class Login(auth_views.LoginView):
    template_name="core/login.html"
    authentication_form = LoginForm

def logoutView(request):
    logout(request)
    return redirect('/')