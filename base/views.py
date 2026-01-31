from django.shortcuts import render , redirect
from .models import FlightModel,SeatClass, PassengerDetail
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    print(request.GET)
    if 'from_city' in request.GET and 'to_city' in request.GET:
        from_city=request.GET['from_city']
        to_city=request.GET['to_city']
        flights=FlightModel.objects.filter(
            Q(departure_city__icontains=from_city) & Q(destination_city__icontains=to_city)
        )
    else:
        flights=FlightModel.objects.all()
    return render(request, 'home.html', {'flights':flights})
@login_required(login_url='login_')

def bookNow(request, pk):
    flight = FlightModel.objects.get(id=pk)
    seat_classes = SeatClass.objects.all()

    SEAT_LIMITS = {
        "First_class (1-100)": 100,
        "Business(1-20)": 20,
        "Economy(1-60)": 60,
    }

    if request.method == 'POST':
        seat_class = request.POST['seat_class']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        adhaar = request.POST['adhaar']
        age = request.POST['age']

        if not all([seat_class, name, email, phone, adhaar, age]):
            return render(request, 'booknow.html', {
                'data': flight,
                'seat_classes': seat_classes,
                'error': "Please fill all details"
            })

        seat_class_instance = SeatClass.objects.get(class_name=seat_class)

        # find booked seats
        booked_seats = PassengerDetail.objects.filter(
            flight=flight,
            seat_class=seat_class_instance,
            is_delete=False
        ).values_list('seat_number', flat=True)

        max_seats = SEAT_LIMITS[seat_class]

        # auto assign seat
        assigned_seat = None
        for i in range(1, max_seats + 1):
            if str(i) not in booked_seats:
                assigned_seat = i
                break

        if not assigned_seat:
            return render(request, 'booknow.html', {
                'data': flight,
                'seat_classes': seat_classes,
                'error': "Seats are full in this class"
            })

        # save booking
        PassengerDetail.objects.create(
            user=request.user,
            flight=flight,
            seat_class=seat_class_instance,
            name=name,
            email=email,
            phone=phone,
            adhaar=adhaar,
            age=age,
            seat_number=str(assigned_seat)
        )

        return redirect('booking')

    return render(request, 'booknow.html', {
        'data': flight,
        'seat_classes': seat_classes
    })

@login_required(login_url='login_')
def booking(request):
    passenger=PassengerDetail.objects.filter(
        user=request.user,
        is_delete=False
        )
    return render(request, 'booking.html', {'passenger':passenger})

@login_required(login_url='login_')
def history(request):
    all_data=PassengerDetail.objects.filter(
        user=request.user,
        is_delete=True)
    return render(request, 'history.html',{'all_data':all_data})


@login_required(login_url='login_')
def delete_(request,pk):
    data=PassengerDetail.objects.get(
        id=pk,
        user=request.user
    )
    data.is_delete=True
    data.save()
    return redirect('history')
@login_required(login_url='login_')
def delete_permanently(request,pk):
    data=PassengerDetail.objects.get(
        id=pk,
        user=request.user)
    data.delete()
    return redirect('history')
@login_required(login_url='login_')
def restore(request, pk):
    data=PassengerDetail.objects.get(
        id=pk,
        user=request.user
        )
    data.is_delete=False
    data.save()
    return redirect('booking')

@login_required(login_url='login_')
def restore_all(request):
    all_data=PassengerDetail.objects.filter(
        user=request.user,
        is_delete=True)
    for data in all_data:
        data.is_delete=False
        data.save()
    return redirect('booking')

@login_required(login_url='login_')
def delete_all(request):
    all_data=PassengerDetail.objects.filter(
        user=request.user,
        is_delete=True)
    all_data.delete()
    return redirect('history')

def support(request):
    return render(request, 'support.html')

def about(request):
    return render(request, 'about.html')