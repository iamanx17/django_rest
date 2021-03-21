from django.shortcuts import render
from .models import student
from .serializers import studentserializer,AccountSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User


# Create your views here.

class StudentApi(ListCreateAPIView):
    queryset=student.objects.all()
    serializer_class=studentserializer


class StudentRUDAPI(RetrieveUpdateDestroyAPIView):
    queryset=student.objects.all()
    serializer_class=studentserializer



class UserAccount(ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=AccountSerializer


class UserUpdateAccount(RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=AccountSerializer
