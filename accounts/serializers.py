from rest_framework import serializers
from django.db import models
from accounts.models import Coffee
from rest_framework import exceptions
from django.contrib.auth import authenticate,login

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields  = ('id','Coffee_name','Price')



