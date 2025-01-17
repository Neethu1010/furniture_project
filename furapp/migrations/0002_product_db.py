# Generated by Django 5.1.2 on 2024-10-14 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(blank=True, max_length=100, null=True)),
                ('Product_name', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('MRP', models.IntegerField(blank=True, null=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('Country', models.CharField(blank=True, max_length=100, null=True)),
                ('Manufactured', models.CharField(blank=True, max_length=100, null=True)),
                ('Product_Image1', models.ImageField(blank=True, null=True, upload_to='Product_Images')),
                ('Product_Image2', models.ImageField(blank=True, null=True, upload_to='Product_Images')),
                ('Product_Image3', models.ImageField(blank=True, null=True, upload_to='Product_Images')),
            ],
        ),
    ]
