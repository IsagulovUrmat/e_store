# Generated by Django 3.1.5 on 2021-02-12 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_order_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='wallet',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
