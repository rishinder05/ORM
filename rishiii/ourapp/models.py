from django.db import models
from django.contrib import admin
class vehicle_DB(models.Model):
    Veh_No=models.IntegerField(primary_key=True)
    Veh_Name=models.CharField(max_length=10)
    Name=models.CharField(max_length=10)
    Dob=models.DateField()
    Address=models.TextField()
    Mobile=models.IntegerField()
class vehicle_DBAdmin(admin.ModelAdmin):
    list_display=["Veh_No","Veh_Name","Name","Dob","Address","Mobile"]