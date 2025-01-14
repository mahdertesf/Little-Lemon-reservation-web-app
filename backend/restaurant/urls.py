from django.urls import path , include
from .views import MenuItemView,SingleMenuItemView , BookingViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('menu/',MenuItemView.as_view(),name='menu'),
    path('menu/<int:pk>/',SingleMenuItemView.as_view(),name='single-menu'),
   
]