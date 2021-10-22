## @brief Models for the instructor app.

from django.db import models
from django.contrib.auth.models import User


# This class represents the instructors enrolled in the website
class Instructor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    information = models.CharField(max_length=1000,default=1)

    def __str__(self):
        return self.name


# This class represents the courses.
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    course_logo = models.FileField(default=1)

    def __str__(self):
        return self.name


# This class represents the assignments in a course.
class Assignment(models.Model):
    description = models.CharField(max_length=1000, default='')
    file = models.FileField(default='')
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    post_time = models.CharField(max_length=100)
    deadline = models.CharField(max_length=100)


# This class represents the submissions for an assignment.
class Submission(models.Model):
    file_submitted = models.FileField(default='')
    time_submitted = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE, default=1)







