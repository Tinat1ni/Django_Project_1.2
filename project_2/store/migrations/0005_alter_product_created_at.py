# Generated by Django 5.1.2 on 2024-10-26 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
