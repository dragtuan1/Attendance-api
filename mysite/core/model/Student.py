from django.db import models
#from core.model import Attendance, Schedule

# Create your models here.
class Student(models.Model):
    codestudent = models.TextField(default='')
    name = models.TextField(default='')
    phone = models.TextField(default='')
    birthday = models.TextField(default='')
    sex = models.BooleanField(default=True)  
    baseclass = models.TextField(default='')
    status = models.IntegerField(default=0)
    urlavatar = models.TextField(default='')
    urlattend = models.TextField(default='')
    schedule = models.ForeignKey('core.Schedule', on_delete=models.CASCADE,related_name='schedules',null=True)
    attendance = models.ForeignKey('core.Attendance', on_delete=models.CASCADE,related_name='attendances',null=True)
    #attendance_id = models.TextField(default='')
    def __str__(self):
        return self.name