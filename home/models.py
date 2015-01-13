from django.db import models

class Users(models.Model):
    user_id = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    
class Board(models.Model):
    subject = models.CharField(max_length=100, default='')
    content = models.CharField(default='', max_length=1000)
    date = models.DateTimeField()