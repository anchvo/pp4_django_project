# Generated by Django 4.2.19 on 2025-02-15 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_appointments', '0021_delete_features_alter_doctor_features'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
