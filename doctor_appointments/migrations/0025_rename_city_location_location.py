# Generated by Django 4.2.19 on 2025-02-15 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_appointments', '0024_rename_location_location_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='city',
            new_name='location',
        ),
    ]
