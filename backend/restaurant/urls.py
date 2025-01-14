from django.urls import path , include
from .views import MenuItemView,SingleMenuItemView , BookingViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu/',MenuItemView.as_view(),name='menu'),
    path('menu/<int:pk>/',SingleMenuItemView.as_view(),name='single-menu'),
    path('api-token-auth/', obtain_auth_token, name='api_token-auth'),
    
   
]