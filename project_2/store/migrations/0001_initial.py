# Generated by Django 5.1.2 on 2024-10-23 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('weight', models.FloatField(help_text='enter product weight in kg')),
                ('country_of_origin', models.CharField(max_length=255)),
                ('quality', models.CharField(max_length=30)),
                ('product_check', models.CharField(max_length=30)),
                ('min_weight', models.FloatField(help_text='minimum weight in kg')),
                ('organic', models.BooleanField(default=False)),
                ('fresh', models.BooleanField(default=False)),
                ('sales', models.BooleanField(default=False)),
                ('discount', models.BooleanField(default=False)),
                ('expired', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category')),
            ],
        ),
    ]