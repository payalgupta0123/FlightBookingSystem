from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class FlightModel(models.Model):
    airline=models.CharField(max_length=100)
    flight_name=models.CharField(max_length=100)
    flight_no=models.CharField(max_length=20)
    departure_city=models.CharField(max_length=100)
    destination_city=models.CharField(max_length=100)
    departure_time=models.TimeField()
    date=models.DateField()
    price=models.IntegerField() 

class SeatClass(models.Model):
    class_name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.class_name

class PassengerDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight=models.ForeignKey(FlightModel, on_delete=models.CASCADE)
    seat_class=models.ForeignKey(SeatClass, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    adhaar=models.CharField(max_length=12)
    age=models.IntegerField()
    seat_number=models.CharField(max_length=10)
    is_delete=models.BooleanField(default=False)

    class Meta:
        unique_together=('flight', 'seat_class', 'seat_number')
