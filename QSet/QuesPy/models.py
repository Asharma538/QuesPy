from django.db import models
import datetime

# Create your models here.
class Question(models.Model):
    source = models.CharField(max_length = 200)
    status = models.CharField(max_length = 200)
    topic = models.CharField(max_length = 200)
    body_q = models.TextField(max_length = 200)
    image_q = models.ImageField()
    opt1 = models.TextField()
    opt2 = models.TextField()
    opt3 = models.TextField()
    opt4 = models.TextField()
    image_of_quetionop1 = models.ImageField()
    image_of_quetionop2 = models.ImageField()
    image_of_quetionop3 = models.ImageField()
    image_of_quetionop4 = models.ImageField()
    date = models.DateField(default = datetime.date.today)
    time = models.TimeField(default = datetime.datetime.now())

    def __str__(self):
        return self.source + " " + self.status