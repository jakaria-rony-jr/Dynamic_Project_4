from django import forms
from .models import BookingForm,ContactForm

class Booking_f(forms.ModelForm):
    class Meta:
        model = BookingForm
        fields = "__all__"


class Contact_f(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = "__all__"