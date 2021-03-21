from django.contrib import admin
from django.urls import path, include
from v5 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.StudentApi.as_view()),
    path('<int:pk>/',views.StudentRUDAPI.as_view()),
    path('accounts/',views.UserAccount.as_view()),
    path('accounts/<int:pk>',views.UserAccount.as_view()),
]
