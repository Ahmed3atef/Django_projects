from django.urls import path
from shops import views

urlpatterns = [
    path('', views.Home.as_view(), name="index")
]