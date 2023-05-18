from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer,TodoSerializer
from django.contrib.auth.models import User
from .models import Todo
from django.http import HttpResponse
from django.core import serializers
import json


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


    def create_todo(self,request):
        
        todo=Todo.objects.create(title=request.POST.get("title",''),
                                 description=request.POST.get("description",''),
                                 user=request.user)
        serializedObj=serializers.serialize('json',[todo,])
        return HttpResponse(serializedObj,content_type='application/json')
    