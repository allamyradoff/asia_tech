# Generated by Django 4.0.4 on 2022-12-27 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obyawleniya', '0005_alter_ad_image_alter_ad_image_2_alter_ad_image_3'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_ads/'),
        ),
    ]
