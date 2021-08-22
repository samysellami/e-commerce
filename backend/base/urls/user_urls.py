from django.contrib import admin
from django.urls import path
from base.views import user_views as views

from base.utils import MyTokenObtainPairView

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', views.registerUser, name="register"),
    path('profile/', views.getUserProfile, name="users-profile"),
    path('profile/update/', views.upadateUserProfile, name="users-profile-update"),
    path('', views.getUsers, name="users"),
]
