# Generated by Django 4.0.6 on 2022-10-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_sale_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale_percent',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]