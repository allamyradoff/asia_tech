# Generated by Django 4.0.6 on 2023-01-26 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_rename_variation_orderproduct_variations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address_line_2',
        ),
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='country',
        ),
    ]
