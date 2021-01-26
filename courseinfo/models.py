from django.db import models

class CourseInfo(models.Model):
    cource_cd = models.CharField(max_length=7) 
    cource_nm = models.CharField(max_length=100) 
    cource_info = models.CharField(max_length=1000) 
    subject_cd = models.CharField(max_length=2) 

    def __str__(self):
        return self.cource_cd
