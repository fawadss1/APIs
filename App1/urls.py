from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('students', views.students, name="students"),
    path('students/student<int:pk>', views.student_details, name="student Details"),
]
