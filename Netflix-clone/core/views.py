from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from core.models import Movie, MovieList
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import re

@login_required(login_url='login')
def index(request):
    movies = Movie.objects.all()
    featured_movie = movies[len(movies)-1]
    return render(request, 'index.html', {
        'movies':movies,
        'featured_movie': featured_movie,
    })


def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request ,username=username, password=password)
        if user is not None:
            auth_login( request, user)
            return redirect('index')
        else:
            messages.error(request,"invalid login")
    return render(request, 'login.html')

def signup(request):
    
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'this email used before !')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'this username taken !')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    email = email,
                    username = username,
                    password = password
                )
                user.save()
                user = authenticate(request, username=username, password = password)
                if user is not None:
                    auth_login( request, user)
                    return redirect('index')
                else:
                    messages.error(request,"invalid login")
        else:
            messages.info(request, "Password not matching !!")
            return redirect('signup')
    return render(request,'signup.html')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('index')

@login_required
def movie(request, pk):
    movie_uuid = pk
    movie = Movie.objects.get(uu_id=movie_uuid)
    
    context = {
        'movie_details': movie
    }
    
    return render(request, 'movie.html', context)

@login_required
def my_list(request):
    user = request.user
    userList = MovieList.objects.filter(owner_user = user)
    user_movie_list = []

    for movie in userList:
        user_movie_list.append(movie.movie)
    
    return render(request, 'my_list.html',{
        'movies': user_movie_list
    })

@login_required(login_url='login')
def add_to_list(request):
    if request.method == 'POST':
        movie_url_id = request.POST.get('movie_id')
        uuid_pattern = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
        match = re.search(uuid_pattern, movie_url_id)
        movie_id = match.group() if match else None

        movie = get_object_or_404(Movie, uu_id=movie_id)
        movie_list, created = MovieList.objects.get_or_create(owner_user=request.user, movie=movie)

        if created:
            response_data = {'status': 'success', 'message': 'Added ✓'}
        else:
            response_data = {'status': 'info', 'message': 'Movie already in list'}

        return JsonResponse(response_data)
    else:
        # return error
        return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

@login_required(login_url = 'login')
def search(request):
    if request.method == "POST":
        search_term = request.POST['search_term']
        movies = Movie.objects.filter(title__icontains=search_term)
        return render(request, 'search.html',{
            'movies':movies,
            'search_term':search_term
        })
    else:
        return redirect('index')

@login_required
def genre(request,pk):
    movie_genre = pk
    movies = Movie.objects.filter(genre=movie_genre)
    return render(request, 'genre.html', {
        'movies':movies,
        'movie_genre':movie_genre
    })