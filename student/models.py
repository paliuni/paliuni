from django.db import models
from courseinfo.models import CourseInfo 
from django.contrib.auth.models import User

class RegCourses(models.Model):
    student = models.ForeignKey(User, models.CASCADE) 
    courses = models.ManyToManyField(CourseInfo, related_name='selected_course')

    def __str__(self):
        return f'{self.student}'


