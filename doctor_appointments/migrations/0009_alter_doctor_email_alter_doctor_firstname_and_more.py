# Generated by Django 4.2.19 on 2025-02-14 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_appointments', '0008_alter_doctor_email_alter_patient_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='firstname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='full_address',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='lastname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='location',
            field=models.CharField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialisation',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='firstname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='lastname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
