import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from core.models import PropertyPurchaser, Property, CustomUser

# Ensure we have a sample user
user, created = CustomUser.objects.get_or_create(
    username='sampleuser',
    defaults={
        'email': 'sampleuser@example.com',
        'password': 'samplepassword',  # Note: For actual use, use proper password hashing
        'user_role': 'property_purchaser',
    }
)

# Create a sample PropertyPurchaser if not already created
property_purchaser, created = PropertyPurchaser.objects.get_or_create(
    user=user,
    defaults={
        'phone_number': '1234567890',
        'specialties': 'Residential',
        'service_areas': 'New York',
    }
)

# Delete all existing properties associated with this property purchaser
Property.objects.filter(property_purchaser=property_purchaser).delete()

print("All existing property records deleted successfully.")