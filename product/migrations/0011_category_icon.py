# Generated by Django 4.0.6 on 2022-10-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_product_sale_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]