
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='site-home'),
    path('about/', views.home, name='site-about'),
    path('profile/', views.profile_update, name='profile-update')
]
