# Generated by Django 4.0.6 on 2023-01-30 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0016_remove_slider_mobile_banner_minislider_mobile_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='vipad',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
