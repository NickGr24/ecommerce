# Generated by Django 3.2 on 2021-05-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_total',
            field=models.FloatField(default=5.99),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(default=5.99),
        ),
    ]
