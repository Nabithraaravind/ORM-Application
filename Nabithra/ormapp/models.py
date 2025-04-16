from django.db import models
from django.contrib import admin
class Movies (models.Model):
    USERID=models.CharField(max_length=20,help_text="USER_ID")
    USERNAME=models.CharField(max_length=100)
    MOVIENAME=models.CharField(max_length=100)
    NOOFSEATS=models.IntegerField()
    EMAIL=models.EmailField()

class MoviesAdmin(admin.ModelAdmin):
    list_display=('USERID','USERNAME','MOVIENAME','NOOFSEATS','EMAIL')