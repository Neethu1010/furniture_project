# Generated by Django 5.1.2 on 2024-11-19 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_carddb_prod_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carddb',
            name='Prod_image',
            field=models.ImageField(blank=True, null=True, upload_to='cart_images'),
        ),
    ]
