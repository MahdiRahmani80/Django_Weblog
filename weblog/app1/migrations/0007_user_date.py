# Generated by Django 3.2.2 on 2021-05-07 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 7, 11, 23, 35, 788928)),
        ),
    ]