from django import forms
from .models import Booking, AvailableDay

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_time', 'end_time']

class AvailableDayForm(forms.ModelForm):
    class Meta:
        model = AvailableDay
        fields = ['day', 'is_available']