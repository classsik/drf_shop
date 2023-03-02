from django.contrib import admin
from django.urls import path
from main.views import CRUDProduct, CRUDManufacturer, CRUDCategory

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', CRUDProduct.as_view()),
    path('products/<int:pk>/', CRUDProduct.as_view()),
    path('manufacturers/', CRUDManufacturer.as_view()),
    path('manufacturers/<int:pk>/', CRUDManufacturer.as_view()),
    path('categories/', CRUDCategory.as_view()),
    path('categories/<int:pk>/', CRUDCategory.as_view()),
]
