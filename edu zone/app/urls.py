from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('', views.index, name='home'),  # Uy sahifasi sifatida login sahifasini ko'rsatish
]
