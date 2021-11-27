from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('students', views.students, name="students"),
    path('students/std<int:pk>', views.student_details, name="student Details"),
]
