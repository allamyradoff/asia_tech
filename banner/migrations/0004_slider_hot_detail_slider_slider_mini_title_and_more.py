# Generated by Django 4.0.6 on 2022-10-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0003_remove_slider_hot_detail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='hot_detail',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='slider_mini_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='slider',
            name='slider_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
