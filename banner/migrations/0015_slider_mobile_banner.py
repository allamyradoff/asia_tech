# Generated by Django 4.0.6 on 2023-01-30 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0014_checkoutbanner'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='mobile_banner',
            field=models.ImageField(blank=True, null=True, upload_to='mobile_banner/'),
        ),
    ]