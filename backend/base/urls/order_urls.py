from django.contrib import admin
from django.urls import path
from base.views import order_views as views


urlpatterns = [

    path('', views.OrderListAPIView.as_view(), name="orders"),
    # path('', views.getOrders, name="orders"),

    path('add/', views.OrderAPIView.as_view(), name="orders-add"),
    # path('add/', views.addOrderItems, name="orders-add"),

    path('myorders/', views.MyOrderListAPIView.as_view(), name="myorders"),
    # path('myorders/', views.getMyOrders, name="myorders"),

    path('<str:pk>/deliver/', views.updateOrderToDelivered, name="order-delivered"),

    path('<str:pk>/', views.OrderAPIView.as_view(), name="user-order"),
    # path('<str:pk>/', views.getOrderById, name="user-order"),

    path('<str:pk>/pay/', views.updateOrderToPaid, name="order-payed"),
]
