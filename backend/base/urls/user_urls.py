from django.contrib import admin
from django.urls import path
from base.views import user_views as views

from base.utils import MyTokenObtainPairView

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('register/', views.RegisterUserAPIView.as_view(), name="register"),
    # path('register/', views.registerUser, name="register"),

    path('profile/', views.UserProfileAPIView.as_view(), name="users-profile"),
    # path('profile/', views.getUserProfile, name="users-profile"),

    path('profile/update/', views.UserProfileAPIView.as_view(), name="users-profile-update"),
    # path('profile/update/', views.updateUserProfile, name="users-profile-update"),

    path('', views.UserListAPIView.as_view(), name="users"),
    # path('', views.getUsers, name="users"),

    path('<str:pk>/', views.UserAPIView.as_view(), name="user"),
    # path('<str:pk>/', views.getUserById, name="user"),

    path('update/<str:pk>/', views.UserAPIView.as_view(), name="user-update"),
    # path('update/<str:pk>/', views.updateUser, name="user-update"),

    path('delete/<str:pk>/', views.UserAPIView.as_view(), name="user-delete"),
    # path('delete/<str:pk>/', views.deleteUser, name="user-delete"),
]
