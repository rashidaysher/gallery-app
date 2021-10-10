# Generated by Django 3.2.8 on 2021-10-10 13:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('picha', '0006_auto_20211008_2147'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['date']},
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_category',
            new_name='pic_category',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_location',
            new_name='pic_location',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='pic',
            new_name='picture',
        ),
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
        migrations.RemoveField(
            model_name='image',
            name='picha',
        ),
        migrations.AddField(
            model_name='image',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='pic_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
