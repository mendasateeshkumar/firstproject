# Generated by Django 4.0.4 on 2022-06-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sateesh', '0002_rename_name_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_password',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_phno',
            field=models.IntegerField(max_length=20),
        ),
    ]
