# Generated by Django 5.0.1 on 2024-02-05 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_useripaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useripaddress',
            name='timestamp',
        ),
    ]
