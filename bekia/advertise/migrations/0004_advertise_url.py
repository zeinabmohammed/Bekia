# Generated by Django 2.1.5 on 2019-06-23 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0003_advertise_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertise',
            name='url',
            field=models.SlugField(blank=True, max_length=500, unique=True),
        ),
    ]