
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

def home(request):
    return HttpResponse("<h1>Добро пожаловать в Habits Tracker API</h1>")

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('habits/', include('habits.urls')),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
