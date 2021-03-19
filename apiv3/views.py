from rest_framework.response import Response
from .models import student
from .serializers import studentSerializer
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.


class StudentApi(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=student.objects.get(id=id)
            serializer=studentSerializer(stu)
            return Response(serializer.data)
        stu=student.objects.all()
        serializer=studentSerializer(stu,many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer=studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self,request,pk,format=None):
        id=pk
        stu=student.objects.get(pk=id)
        serializer=studentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk ,format=None):
        id=pk
        stu=student.objects.get(pk=id)
        serializer=studentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk, format=None):
        id=pk
        stu=student.objects.get(pk=id)
        stu.delete()  
        return Response({'msg':'Data deleted'})
       




