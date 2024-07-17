# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse  

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('client', 'Client'),
        ('property_purchaser', 'Property Purchaser'),
        ('salesperson', 'Salesperson'),
    )
    user_role = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='client')
    address = models.CharField(max_length=255, null=True, blank=True)

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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    land_size = models.CharField(max_length=50)
    image = models.ImageField(upload_to='property_images/', null=True, blank=True)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE, related_name='properties', null=True, blank=True)

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse('property_detail', args=[str(self.id)])

class Inquiry(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    offer = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    timeline = models.CharField(max_length=100, default='As soon as possible')
    availability = models.CharField(max_length=100, default='Anytime')
    status = models.CharField(max_length=50, default='Pending')
    estimated_closing_time = models.DateTimeField(null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    response = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Inquiry for {self.property.address} by {self.client.username}"

class Review(models.Model):
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, default=1)  # Assume property with ID 1 exists
    rating = models.IntegerField()
    review_text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.client.username} for {self.property.address}"
