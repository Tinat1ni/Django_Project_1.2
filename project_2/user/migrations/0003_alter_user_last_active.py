# Generated by Django 5.1.2 on 2024-10-31 14:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_last_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_active',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 31, 14, 27, 16, 321301, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
