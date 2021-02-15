# Generated by Django 3.1.5 on 2021-02-14 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_profile_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='sale_amount',
            field=models.FloatField(default=0.1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(default=datetime.date(2021, 2, 14)),
        ),
    ]