# Generated by Django 3.2.2 on 2021-05-06 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_user_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isVerified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='site',
            field=models.URLField(blank=True, null=True),
        ),
    ]