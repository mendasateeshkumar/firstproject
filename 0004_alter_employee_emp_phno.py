# Generated by Django 4.0.4 on 2022-06-07 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sateesh', '0003_alter_employee_emp_password_alter_employee_emp_phno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_phno',
            field=models.BigIntegerField(),
        ),
    ]
