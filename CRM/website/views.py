from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import forms
from . import models

def home(request):
    records = models.Record.objects.all()
    
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Been Logged In')
            return redirect('home')
        else:
            messages.success(request, "Enter correct username or password")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You Logged out")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "You Created an account successfully")
            return redirect('home')
    else:
        form = forms.SignUpForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record= models.Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must logged in to view that page")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = models.Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Deleted")        
        return redirect('home')
    else:
        messages.success(request, "You must logged in ")
        return redirect('home')

def add_record(request):
    form = forms.AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added")
                return redirect('home')
        return render(request, 'add_record.html', {"form": form})
    else:
        messages.success(request, "You must logged in ")
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = models.Record.objects.get(id=pk)
        form = forms.AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated")
            return redirect('home')
        return render(request, 'update_record.html', {"form": form})
    else:
        messages.success(request, "You must logged in ")
        return redirect('home')