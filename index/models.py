from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class chart(models.Model):
    choie = [
        ('Time Chart', 'Time Chart'),
        ('Integer Chart', 'Integer Chart')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    choices = models.CharField(max_length=100, choices=choie)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']


class index(models.Model):
    chart = models.ForeignKey(
        chart, related_name="chart_index", blank=True, null=True, on_delete=models.DO_NOTHING)
    int_value = models.IntegerField(blank=True, null=True)
    time_value = models.TimeField(blank=True, null=True)
    date_create = models.DateTimeField(auto_now_add=True)

    @property
    def labels(self):
        return f"{self.date_create:%m/%d}"

    @property
    def time(self):
        return f"{self.time_value:%h}"

    # class Meta:
    #     ordering = ['-date_create']
