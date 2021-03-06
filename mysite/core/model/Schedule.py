from django.db import models

class Schedule(models.Model):
    #id = models.IntegerField(primary_key=True, max_length=255)
    subject = models.TextField(default='')
    timestart = models.TextField(default='')
    timeend = models.TextField(default='')
    room = models.TextField(default='')
    serial = models.TextField(default='')
    total = models.TextField(default='')
    account = models.ForeignKey('core.Account', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.subject