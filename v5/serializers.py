from rest_framework import serializers
from .models import student
from django.contrib.auth.models import User

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields="__all__"


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','username','first_name','last_name','password']