from django.urls import path
from .views import ProductsView,ProfileViewAdmin,Delete,CreateProductView,EditProfileView

app_name = 'salar'

urlpatterns = [
    path('products/',ProductsView.as_view(),name='products'),
    path('delete/<int:id>/',Delete.as_view(),name='delete'),
    path('update/<int:id>/',Delete.as_view(),name='update'),
    path('products/create/', CreateProductView.as_view(), name='create_product'),
    path('dashboard/',ProfileViewAdmin.as_view(),name='dashboard'),
]