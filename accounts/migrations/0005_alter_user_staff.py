# Generated by Django 3.2 on 2021-05-16 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='staff',
            field=models.BooleanField(default=True),
        ),
    ]
