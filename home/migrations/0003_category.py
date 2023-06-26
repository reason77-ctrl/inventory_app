# Generated by Django 4.2.2 on 2023-06-16 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Category Name')),
                ('fa_image', models.CharField(max_length=50, verbose_name='Fas Fa Image')),
            ],
        ),
    ]
