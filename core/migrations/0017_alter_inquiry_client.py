# Generated by Django 5.0.7 on 2024-07-24 06:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_property_garage_property_number_of_bathrooms_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inquiries', to=settings.AUTH_USER_MODEL),
        ),
    ]
