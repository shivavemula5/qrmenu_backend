from django.urls import path 

from rest_framework_nested import routers

from core.api import views

router = routers.SimpleRouter()
router.register('places',views.PlaceViewSet,basename='places')

categoryNestedRouter = routers.NestedSimpleRouter(router,'places',lookup='place')
categoryNestedRouter.register('categories',views.CategoryViewSet,basename='categories')

menuNestedRouter = routers.NestedSimpleRouter(categoryNestedRouter,'categories',lookup='categories')
menuNestedRouter.register('menu',views.MenuItemViewSet,basename='menu')

router.register('menu',views.PlaceDetailViewSet,basename='placedetail')

urlpatterns = [
    
] + router.urls + categoryNestedRouter.urls + menuNestedRouter.urls
