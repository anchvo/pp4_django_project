# Generated by Django 4.2.19 on 2025-02-15 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_appointments', '0025_rename_city_location_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='location',
        ),
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='location',
            name='doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='doctor_appointments.doctor'),
        ),
        migrations.AddField(
            model_name='specialisation',
            name='doctor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='doctor_appointments.doctor'),
        ),
        migrations.AlterField(
            model_name='specialisation',
            name='specialisation',
            field=models.CharField(blank=True),
        ),
    ]
