from django.db import models # type: ignore
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from datetime import datetime
from django.utils import timezone
from geopy.geocoders import GoogleV3
from geopy.exc import GeocoderTimedOut  
import logging


GOOGLE_API_KEY ='AIzaSyAOcYGAH1Ye5f0nRxF6YJjdLlHycdSrVQw'

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('client', 'Client'),
        ('property_purchaser', 'Property Purchaser'),
        ('salesperson', 'Salesperson'),
    )
    user_role = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='client')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    office_address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

class PropertyPurchaser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    specialties = models.TextField()
    service_areas = models.TextField()

    def __str__(self):
        return self.user.username

class Salesperson(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50)

class Property(models.Model):
    property_purchaser = models.ForeignKey(PropertyPurchaser, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    description = models.TextField()
    price = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    land_size = models.CharField(max_length=20)
    image = models.ImageField(upload_to='property_images/', null=True, blank=True)
    number_of_bedrooms = models.CharField(max_length=5, null=True, blank=True)
    number_of_bathrooms = models.CharField(max_length=5, null=True, blank=True)
    garage = models.CharField(max_length=5, null=True, blank=True)
    year_built = models.CharField(max_length=4, null=True, blank=True)
    zip_code = models.CharField(max_length=5, null=True, blank=True)  # Ensure zip code is 5 digits
    state = models.CharField(max_length=2, null=True, blank=True)  # State abbreviation
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.is_address_changed():
            full_address = self.address
            if self.state:
                full_address += f", {self.state}"
            if self.zip_code:
                full_address += f" {self.zip_code}"
                
                geolocator = GoogleV3(api_key=GOOGLE_API_KEY)
                try:
                    location = geolocator.geocode(full_address)
                    if location:
                        self.latitude = location.latitude
                        self.longitude = location.longitude
                    else:
                        logging.warning(f"Geocoding failed for address: {full_address}")
                except GeocoderTimedOut:
                    logging.error(f"Google Maps geocoding API timed out for address: {full_address}")
                except Exception as e:
                    # Log or handle the error as appropriate
                    logging.error(f"Error geocoding address {full_address}: {e}")
        if self.latitude is not None and self.longitude is not None:
            self.location = Point(self.longitude, self.latitude)
        super(Property, self).save(*args, **kwargs)
    
    def is_address_changed(self):
        """Helper method to check if address, state, or zip code has been modified by comparing the current value with the original value."""
        if self.pk: 
            original = self.__class__.objects.get(pk=self.pk)
            return (original.address != self.address or original.state != self.state or original.zip_code != self.zip_code)
        return True

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse('property_detail', args=[str(self.id)])
    
class Inquiry(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='inquiries')
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    offer = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    timeline = models.CharField(max_length=100, default='As soon as possible')
    availability = models.CharField(max_length=100, default='Anytime')
    status = models.CharField(max_length=50, default='Pending')
    estimated_closing_time = models.DateTimeField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    response = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created


    def __str__(self):
        return f"Inquiry for {self.property.address} by {self.client.username}"

class Review(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, default=1)
    rating = models.IntegerField()
    review_text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.client.username} for {self.property.address}"

class AdditionalPhoto(models.Model):
    property = models.ForeignKey(Property, related_name='additional_photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='additional_photos/')
