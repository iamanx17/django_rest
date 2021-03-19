from django.urls import path
from . import views

urlpatterns = [
    path('api/',views.studentCreate.as_view()),
    path('apir/<int:pk>',views.studentRetrive.as_view()),
    path('apiu/<int:pk>/',views.studentUpdate.as_view()),
    path('apid/<int:pk>/',views.studentDestroy.as_view()),
 
]
