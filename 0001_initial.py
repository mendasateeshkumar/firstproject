# Generated by Django 4.0.4 on 2022-06-07 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('emp_name', models.CharField(max_length=35)),
                ('emp_phno', models.IntegerField()),
                ('emp_mailid', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('emp_password', models.IntegerField()),
            ],
        ),
    ]
