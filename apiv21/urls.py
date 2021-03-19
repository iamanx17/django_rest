from django.urls import path 
from . import views

urlpatterns = [
    path('api/',views.LCStudentApi.as_view()),
    path('apirud/<int:pk>',views.RUDStudentApi.as_view()),


]
