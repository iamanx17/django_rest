from django.shortcuts import render
from .models import student
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from .serializers import studentSerializer

# Create your views here.
#Generic api view and model class

#Generic api: ListModelMixin view will give you the json data in list 
class studentList(GenericAPIView, ListModelMixin):
    queryset=student.objects.all()
    serializer_class=studentSerializer

    def get(self, request,*args,**kwargs):
        return self.list(request,*args,**kwargs)


#Generic api:CreateModelMixin will give you tool to post data
class studentCreate(GenericAPIView, CreateModelMixin):
    queryset=student.objects.all()
    serializer_class=studentSerializer

    def post(self, request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class studentRetrive(GenericAPIView, RetrieveModelMixin):
    queryset=student.objects.all()
    serializer_class=studentSerializer

    def get(self, request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)


class studentUpdate(GenericAPIView, UpdateModelMixin):
    queryset=student.objects.all()
    serializer_class=studentSerializer

    def put(self, request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class studentDestroy(GenericAPIView, DestroyModelMixin):
    queryset=student.objects.all()
    serializer_class=studentSerializer

    def delete(self, request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)

