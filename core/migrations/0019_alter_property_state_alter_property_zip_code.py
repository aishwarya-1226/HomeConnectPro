# Generated by Django 5.0.7 on 2024-07-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_property_state_property_zip_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='state',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='zip_code',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]