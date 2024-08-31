from django.urls import path
from core import views


urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('signup/',views.signup, name='signup'),
    path('movie/<str:pk>',views.movie, name='movie'),
    path('my-list/', views.my_list, name='mylist'),
    path('add-to-list/', views.add_to_list, name='add-to-list'),
    path('search/', views.search, name='search'),
    path('genre/<str:pk>/',views.genre, name='genre'),
]
