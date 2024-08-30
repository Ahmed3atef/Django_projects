from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import SongViewSet

router = DefaultRouter()
router.register(r'songs', SongViewSet)

urlpatterns = [
    path('', include(router.urls)),
]