from django.shortcuts import render
from .serializers import studentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from .models import student
# Create your views here.

"""
class Studentlist(ListAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer

class studentcreate(CreateAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer


class studentretrieve(RetrieveAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer

class studentupdate(UpdateAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer


class studentdestroy(DestroyAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer

class studentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer
"""
class studentListCreate(ListCreateAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer


class studentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer


#to combine apiview class use apiview combined clas listceateapivieew