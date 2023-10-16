from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Food
from rest_framework import serializers

# Create your views here.

class Foodserializer(serializers.ModelSerializer):
  class Meta:
    model = Food
    fields = '__all__'


@api_view(['GET'])
def fetchfood(request):
  allfood = Food.objects.all()

  serializer = Foodserializer(allfood, many=True)
  
  return Response (serializer.data)

@api_view(['POST'])
def createfood(request):
  print(request.data)
  return Response("the title is ")