# views.py
from django.shortcuts import render, redirect
from .models import Booking, AvailableDay
from .forms import BookingForm, AvailableDayForm
from django.shortcuts import render
from .models import Availability

def availability_view(request):
    availabilities = Availability.objects.all()
    return render(request, 'availability_template.html', {'availabilities': availabilities})

def calendar_view(request):
    bookings = Booking.objects.all()
    # calendar = MyCalendar.objects.get(name='Default')
    return render(request, 'calendar.html', {'bookings': bookings, 'calendar': calendar})

def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_view')
    else:
        form = BookingForm()

    return render(request, 'add_booking.html', {'form': form})

def update_available_days(request):
    if request.method == 'POST':
        form = AvailableDayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_view')
    else:
        form = AvailableDayForm()

    return render(request, 'update_available_days.html', {'form': form})
