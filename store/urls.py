from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers
from pprint import pprint


router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
urlpatterns = router.urls
products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewset,
                         basename='product-reviews')

urlpatterns = router.urls + products_router.urls
