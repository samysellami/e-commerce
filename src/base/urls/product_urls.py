from django.contrib import admin
from django.urls import path
from base.views import product_views as views


urlpatterns = [

    path('', views.ProductListAPIView.as_view(), name="products"),
    # path('', views.getProducts, name="products"),

    path('upload/', views.uploadImage, name="image-upload"),

    path('create/', views.ProductAPIView.as_view(), name="product-create"),
    # path('create/', views.createProduct, name="product-create"),

    path('<str:pk>/reviews/', views.ProductReviewAPIView.as_view(), name="create-review"),
    # path('<str:pk>/reviews/', views.createProductReview, name="create-review"),

    path('top/', views.TopProductListAPIView.as_view(), name="top-products"),
    # path('top/', views.getTopProducts, name="top-products"),

    path('<str:pk>/', views.ProductDetailAPIView.as_view(), name="product"),
    # path('<str:pk>/', views.getProduct, name="product"),

    path('delete/<str:pk>/', views.ProductAPIView.as_view(), name="product-delete"),
    # path('delete/<str:pk>/', views.deleteProduct, name="product-delete"),

    path('update/<str:pk>/', views.ProductAPIView.as_view(), name="product-update"),
    # path('update/<str:pk>/', views.updateProduct, name="product-update"),

]
