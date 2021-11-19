from django.db import models


class Student(models.Model):
    Name = models.CharField(max_length=25)
    Father_Name = models.CharField(max_length=25)
    Roll_No = models.IntegerField()
    School_Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name
