from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter
from pprint import pprint


router = SimpleRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
urlpatterns = router.urls
