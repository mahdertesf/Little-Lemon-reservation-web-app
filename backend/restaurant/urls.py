from django.urls import path , include
from .views import MenuItemView,SingleMenuItemView , BookingViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'tables',BookingViewSet)
urlpatterns = [
    path('menu/',MenuItemView.as_view(),name='menu'),
    path('menu/<int:pk>/',SingleMenuItemView.as_view(),name='single-menu'),
    path('restaurant/booking/',include(router.urls)),
]