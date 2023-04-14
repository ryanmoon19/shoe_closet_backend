from django.shortcuts import render
from rest_framework import generics
from .serializers import ShoesSerializer
from .models import Shoes

# Create your views here.
## POST, GET
class ShoesList(generics.ListCreateAPIView):
    queryset = Shoes.objects.all().order_by('id')
    serializer_class = ShoesSerializer


## /shoes/:id
class ShoesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shoes.objects.all().order_by('id')
    serializer_class = ShoesSerializer