# Generated by Django 3.2.8 on 2021-10-10 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picha', '0007_auto_20211010_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='pic_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='picture',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='pic_name',
            new_name='image_name',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='pic_location',
            new_name='location',
        ),
    ]