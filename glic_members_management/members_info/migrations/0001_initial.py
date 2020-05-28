# Generated by Django 2.2.6 on 2019-10-25 12:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images')),
                ('fullname', models.CharField(max_length=255)),
                ('yearofbirth', models.DateField(default=datetime.datetime.now)),
                ('sex', models.CharField(default='Male', max_length=255)),
                ('job', models.CharField(default='No Job', max_length=255)),
                ('subcity', models.CharField(default='xxxx', max_length=255)),
                ('woreda', models.IntegerField(default=0)),
                ('housenum', models.CharField(default='xxxx', max_length=255)),
                ('phonenum', models.CharField(default='xxxx-xx-xx-xx', max_length=255)),
                ('marriage', models.BooleanField(default=False)),
                ('yearofmarriage', models.DateField(default=datetime.datetime.now)),
                ('childernnum', models.IntegerField(default=0)),
                ('yearofsalvation', models.DateField(default=datetime.datetime.now)),
                ('baptism', models.BooleanField(default=True)),
                ('yearofbaptism', models.DateField(default=datetime.datetime.now)),
                ('prevchurch', models.CharField(default='GLIC', max_length=255)),
                ('death', models.BooleanField(default=False)),
            ],
        ),
    ]