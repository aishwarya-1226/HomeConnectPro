import random
from datetime import timedelta, datetime
from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import Inquiry  # Adjust the import according to your app structure

class Command(BaseCommand):
    help = 'Update inquiries with random recent dates and times'

    def handle(self, *args, **kwargs):
        inquiries = Inquiry.objects.all()
        for inquiry in inquiries:
            random_days = random.randint(1, 90)
            random_date = timezone.now() - timedelta(days=random_days)
            
            # Randomize the time component
            random_hours = random.randint(0, 23)
            random_minutes = random.randint(0, 59)
            random_seconds = random.randint(0, 59)
            
            random_date = random_date.replace(hour=random_hours, minute=random_minutes, second=random_seconds)
            
            inquiry.created_at = random_date
            inquiry.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated inquiries with random recent dates and times'))
