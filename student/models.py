from django.db import models

class Student(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=60)
    dob = models.CharField(max_length=60)
    address = models.CharField(max_length=256)
    phone = models.CharField(max_length=16)
    major = models.CharField(max_length=30)

    def __str__(self):
        return self.student_name