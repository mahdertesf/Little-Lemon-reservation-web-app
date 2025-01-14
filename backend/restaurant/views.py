from django.shortcuts import render
from rest_framework import generics
from .models import Menu,Booking
from .serializers import MenuSerializer
# Create your views here.

class MenuItemView(generics.ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer
    
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer
    