from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .models import student
from .serializers import studentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def student_get(request):
    if request.method=='GET':
        json_data=request.body# it will return a dcitionary {'id':1}
        stream=io.BytesIO(json_data)
        print('stream is')# itt will return stream like <io.BytesIo object>
        print(stream)
        python_data=JSONParser().parse(stream)#it will convert in python data {'id':1}
        id=python_data.get('id',None)
        if id is not None:
            stu=student.objects.get(id=id)
            serializer=studentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu=student.objects.all()
        serializer=studentSerializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    stu=student.objects.all()
    serializer=studentSerializer(stu,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def student_post(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=studentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'data has been saved successfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')

        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    stu=student.objects.all()
    serializer=studentSerializer(stu,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')
    

