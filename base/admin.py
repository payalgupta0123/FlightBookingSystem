from django.contrib import admin
from .models import FlightModel ,PassengerDetail,SeatClass
# Register your models here.
class FlightAdminModel(admin.ModelAdmin):
    list_display=['id', 'airline', 'flight_name','flight_no', 'departure_city','destination_city', 'date', 'price']


class PassengerAdmin(admin.ModelAdmin):
    list_display=['id', 'seat_class','name', 'email', 'phone', 'adhaar', 'age', 'seat_number']

class SeatAdmin(admin.ModelAdmin):
    list_display=['id', 'class_name']


admin.site.register(SeatClass,SeatAdmin)
admin.site.register(PassengerDetail,PassengerAdmin)
admin.site.register(FlightModel,FlightAdminModel)