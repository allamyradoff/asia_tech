# Generated by Django 4.0.6 on 2022-10-07 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_orderproduct_variation_orderproduct_variation'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='ordered',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_ordered',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='product_price',
            field=models.FloatField(),
        ),
    ]
