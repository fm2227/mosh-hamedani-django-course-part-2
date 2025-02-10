from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers


router = DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewset)
products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewset,
                         basename='product-reviews')
urlpatterns = router.urls + products_router.urls
Cartitems_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
Cartitems_router.register(
    'items', views.CartItemViewset, basename='cart-items')
urlpatterns = router.urls + Cartitems_router.urls
