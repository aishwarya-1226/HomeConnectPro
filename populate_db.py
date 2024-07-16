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

# Create a sample PropertyPurchaser
property_purchaser, created = PropertyPurchaser.objects.get_or_create(
    user=user,
    defaults={
        'phone_number': '1234567890',
        'specialties': 'Residential',
        'service_areas': 'New York',
    }
)

# Add sample properties with images
Property.objects.create(
    property_purchaser=property_purchaser,
    address='123 Main St',
    description='A lovely family home',
    price=300000,
    category='Residential',
    land_size='2000 sqft',
    image='property_images/sample_1.jpg'  # Make sure this path is correct and the file exists
)


Property.objects.create(
    property_purchaser=property_purchaser,
    address='456 Elm St',
    description='A modern apartment',
    price=150000,
    category='Residential',
    land_size='800 sqft',
    image='property_images/sample_2.jpg'  # Make sure this path is correct and the file exists
)

Property.objects.create(
    property_purchaser=property_purchaser,
    address='345 Grover St',
    description='A modern apartment',
    price=1580000,
    category='Residential',
    land_size='8000 sqft',
    image='property_images/sample_3.jpg'  # Make sure this path is correct and the file exists
)

Property.objects.create(
    property_purchaser=property_purchaser,
    address='515 Bay St',
    description='A modern apartment',
    price=350000,
    category='Residential',
    land_size='8060 sqft',
    image='property_images/sample_4.jpg'  # Make sure this path is correct and the file exists
)


print("Sample data with images added successfully.")
