from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class People(models.Model):
    
    Names = models.CharField(max_length=100)

    def __str__(self):
        return self.Names

class User(models.Model):
    Name = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    Reg_Number = models.CharField(max_length=8)
    e_mail = models.EmailField()
    Password = models.CharField(max_length=20)

    def __str__(self):
        return self.Reg_Number

class Question(models.Model):
    asker = models.ForeignKey(User , on_delete=models.CASCADE)
    topic = models.CharField(max_length=40)
    body = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)

    def get_asker(self , request):
        asker = request.user()
        return asker

    def get_absolute_url(self):
        return reverse('app:questions')

    def __str__(self):
        return self.topic

class Answer(models.Model):
    answerer = models.ForeignKey(User , on_delete=models.CASCADE)
    qn = models.ForeignKey(Question, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def get_asker(self , request):
        answerer = request.user()
        return answerer

    def get_absolute_url(self):
        return reverse('app:questions')

    def __str__(self):
        return self.body
