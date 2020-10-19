from django.db import models

# Create your models here.

class Car(models.Model):
    SERVICE_CHOICES =[('P','Platinum'),('G','Gold')]
    car_model = models.CharField(max_length=1000)
    car_owner = models.CharField(max_length=1000)
    car_notes = models.CharField(max_length=1000)
    car_number = models.CharField(max_length=300)
    description = models.TextField()
    service_type = models.CharField(choices=SERVICE_CHOICES,blank=True,max_length=1,null=True)
    submission_date = models.DateTimeField()
    year_old = models.IntegerField(null=True)
    servicing = models.ManyToManyField('Service',blank=True)
    

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name