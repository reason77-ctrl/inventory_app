# Generated by Django 4.2.2 on 2023-06-13 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
    ]
