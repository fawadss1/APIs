from django.db import models


class Instructor(models.Model):
    Name = models.CharField(max_length=25)
    Mobile = models.CharField(max_length=25)
    Address = models.CharField(max_length=50)
    Designation = models.CharField(max_length=30)

    def __str__(self):
        return self.Name


class Course(models.Model):
    Name = models.CharField(max_length=50)
    Code = models.CharField(max_length=25)
    Duration = models.CharField(max_length=20)
    Instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Student(models.Model):
    Name = models.CharField(max_length=25)
    Father_Name = models.CharField(max_length=25)
    Roll_No = models.IntegerField()
    School_Name = models.CharField(max_length=50)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
