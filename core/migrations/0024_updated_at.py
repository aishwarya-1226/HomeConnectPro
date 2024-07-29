import random
from django.db import migrations
from django.utils import timezone
from datetime import timedelta

def assign_random_created_at(apps, schema_editor):
    Inquiry = apps.get_model('core', 'Inquiry')
    for inquiry in Inquiry.objects.all():
        # Assign a random date within the last 30 days
        random_days = random.randint(0, 30)
        random_time = timezone.now() - timedelta(days=random_days)
        inquiry.created_at = random_time
        inquiry.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_property_created_at'),  # Replace with the name of your last migration file
    ]

    operations = [
        migrations.RunPython(assign_random_created_at),
    ]
