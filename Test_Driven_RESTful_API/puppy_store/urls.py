
from django.contrib import admin
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("puppies.urls")),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    path("api/schema/", SpectacularAPIView.as_view(),name="schema"),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path('api/shcema/docs/', SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
]
