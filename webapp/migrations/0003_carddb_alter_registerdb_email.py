# Generated by Django 5.1.2 on 2024-11-08 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_registerdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Total_price', models.IntegerField(blank=True, null=True)),
                ('Product_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='registerdb',
            name='Email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
