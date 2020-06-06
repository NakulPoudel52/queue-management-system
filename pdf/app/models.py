from django.db import models

 #Create your models here.

class Hospital(models.Model):
    hospital_name =models.CharField(max_length=64)

    def __str__(self):
        return f"{self.hospital_name}"

class Doctor(models.Model):
    doctor_name =models.CharField(max_length=64)

    def __str__(self):
        return f"{self.doctor_name}"


class Form(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    contact = models.CharField(max_length=12)
    hname = models.ForeignKey(Hospital, on_delete=models.CASCADE,null=True, related_name="hospital")
    dname = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True, related_name="doctor")
    def __str__(self):
        return f"{self.name} {self.email}"

class Time(models.Model):
    time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.time}"