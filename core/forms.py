from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Property, Inquiry, Review, PropertyPurchaser, Salesperson
from django import forms
from .models import Review

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'user_role', 'address']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ['property_purchaser', 'salesperson']  # Exclude both fields from the form

class InquiryForm(forms.ModelForm):
    offer = forms.DecimalField(max_digits=10, decimal_places=2, label='Your Offer')
    timeline = forms.CharField(max_length=100, label='How soon are you looking to buy/rent?')
    availability = forms.CharField(max_length=100, label='Availability to talk')

    class Meta:
        model = Inquiry
        fields = ['offer', 'timeline', 'availability']

class PropertyPurchaserForm(forms.ModelForm):
    class Meta:
        model = PropertyPurchaser
        fields = ['user', 'phone_number', 'specialties', 'service_areas']

class SalespersonForm(forms.ModelForm):
    class Meta:
        model = Salesperson
        fields = ['user', 'license_number']

class SignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'user_role', 'address']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_text']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'review_text': forms.Textarea(attrs={'rows': 4}),
        }