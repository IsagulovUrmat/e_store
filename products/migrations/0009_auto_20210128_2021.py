# Generated by Django 3.1.5 on 2021-01-28 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='latitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='longtitude',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
