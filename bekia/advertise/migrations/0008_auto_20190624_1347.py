# Generated by Django 2.1.5 on 2019-06-24 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0007_auto_20190623_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertise',
            name='url',
        ),
        migrations.AlterField(
            model_name='advertise',
            name='category',
            field=models.CharField(choices=[('vec', 'Vehicles'), ('prop', 'properties'), ('Mobile Phones & Accessories', 'Mobile Phones & Accessories'), ('Electronics & Home Appliances', 'Electronics & Home Appliances'), ('Home & Garden', 'Home & Garden'), ('Fashion & Beauty', 'Fashion & Beauty'), ('pets', 'Pets'), ('Kids&Babies', 'Kids & Babies'), ('sporting Goods &Bikes', 'Sporting'), ('Hobbies Music Art &Books', 'Hobbies,Music,Art & Books'), ('jobs', 'Jobs'), ('Business&Industrial', 'Business & Industrial'), ('services', 'services')], max_length=120),
        ),
    ]
