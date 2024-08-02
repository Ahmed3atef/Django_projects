from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user,name='register'),
    path('record/<int:pk>/', views.customer_record,name='record'),
    path('add_record/', views.add_record,name='add'),
    path('update_record/<int:pk>/', views.update_record,name='update'),
    path('delete_record/<int:pk>/', views.delete_record,name='delete'),
]