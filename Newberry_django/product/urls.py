from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product import views
from .views import ProductsViewSet
router = DefaultRouter()
router.register('Products', ProductsViewSet, basename='Products')

urlpatterns = [
    path('api/', include(router.urls)),
    path('latest-products/', views.LatestProductsList.as_view()),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
]