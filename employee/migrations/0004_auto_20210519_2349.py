# Generated by Django 3.2.3 on 2021-05-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_entryexit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='entryexit',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='staff_profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
