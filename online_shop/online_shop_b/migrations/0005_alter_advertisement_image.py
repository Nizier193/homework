# Generated by Django 4.2 on 2023-08-25 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop_b', '0004_advertisement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='online_shop_b/', verbose_name='изображения'),
        ),
    ]
