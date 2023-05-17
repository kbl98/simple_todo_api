from django.contrib.auth.models import User
from .models import Todo
from rest_framework import serializers




class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']


class TodoSerializer(serializers.HyperlinkedModelSerializer):
        user=UserSerializer()
        class Meta:
            model = Todo
            fields = ['created_at', 'title', 'description','user']
