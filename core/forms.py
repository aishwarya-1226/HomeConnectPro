from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Property, Inquiry, Review, PropertyPurchaser, Salesperson, AdditionalPhoto

class UserRegistrationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True)
    office_address = forms.CharField(max_length=255, required=False)  # Make office_address optional

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'user_role', 'phone_number', 'office_address']

    def clean(self):
        cleaned_data = super().clean()
        user_role = cleaned_data.get('user_role')
        office_address = cleaned_data.get('office_address')

        if user_role in ['salesperson', 'property_purchaser'] and not office_address:
            self.add_error('office_address', 'Office address is required ')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.phone_number = self.cleaned_data['phone_number']
        user.office_address = self.cleaned_data['office_address']
        if user.user_role in ['salesperson', 'property_purchaser']:
            user.is_active = False  # Deactivate account until it is approved manually
        else:
            user.is_active = True  # Client can be active immediately
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['address', 'category', 'description', 'price', 'year_built', 'number_of_bedrooms', 'number_of_bathrooms', 'land_size', 'image','state','zip_code']
        exclude = ['property_purchaser', 'salesperson']

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

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_text']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'review_text': forms.Textarea(attrs={'rows': 4}),
        }

class PropertyBasicForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['address', 'description', 'price', 'category', 'land_size', 'image']

class PropertyAdditionalForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['number_of_bedrooms', 'number_of_bathrooms', 'garage', 'year_built']

class AdditionalPhotosForm(forms.Form):
    photo1 = forms.ImageField(required=False)
    photo2 = forms.ImageField(required=False)
    photo3 = forms.ImageField(required=False)
