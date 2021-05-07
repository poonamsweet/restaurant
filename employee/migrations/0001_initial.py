# Generated by Django 3.2 on 2021-05-03 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('gender', models.CharField(choices=[('Select', 'Select'), ('Male', 'Male'), ('Female', 'Female')], default='select', max_length=32)),
                ('dateofbirth', models.DateField()),
                ('present_location', models.CharField(max_length=30)),
                ('permanent_address', models.CharField(max_length=50)),
                ('local_address', models.CharField(max_length=50)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(blank=True, choices=[('Select', 'Select'), ('Cook', 'Cook'), ('Waiter', 'Waiter'), ('Staff', 'Staff')], default='select', max_length=32, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('gender', models.CharField(blank=True, choices=[('Select', 'Select'), ('Male', 'Male'), ('Female', 'Female')], default='select', max_length=32, null=True)),
                ('dateofbirth', models.DateField(blank=True, null=True)),
                ('present_location', models.CharField(blank=True, max_length=30, null=True)),
                ('permanent_address', models.CharField(blank=True, max_length=50, null=True)),
                ('local_address', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
