## @brief Models for the course app.

from django.db import models
from django.contrib.auth.models import User
from instructor.models import Course
from django.urls import reverse


# This class represents the students enrolled in the website.
class Student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)
    course_list = models.ManyToManyField(Course)

    def __str__(self):
        return self.name


# This class represents the messages displayed in the forum.
class Message(models.Model):
    content = models.TextField(max_length=500)
    course = models.ForeignKey(Course,default=1,on_delete=models.CASCADE)
    sender = models.ForeignKey(User,default=1, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)


# This class represents the notifications receieved by the students.
class Notification(models.Model):
    content = models.TextField(max_length=500)
    course = models.ForeignKey(Course, default=1, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)


# This class represents the resources(lectures/study materials) for a course.
class Resources(models.Model):
    file_resource = models.FileField(default='')
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, default=1, on_delete=models.CASCADE)
