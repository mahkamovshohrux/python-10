from django.shortcuts import render
from rest_framework import generics
from .models import Models10
from .serializers import Serializers10

# Create your views here.
class AllList10(generics.ListCreateAPIView):
    queryset = Models10.objects.all()
    serializer_class = Serializers10
class Idlist10(generics.RetrieveUpdateDestroyAPIView):
    queryset = Models10.objects.all()
    serializer_class = Serializers10
