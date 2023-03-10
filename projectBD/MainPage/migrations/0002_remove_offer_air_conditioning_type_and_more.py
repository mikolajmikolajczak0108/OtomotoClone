# Generated by Django 4.1.5 on 2023-01-23 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainPage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='air_conditioning_type',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='engine_type',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='fuel_type',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='images',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='make',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='model',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='production_year',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='roof_type',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='upholstery',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='user',
        ),
        migrations.AddField(
            model_name='offer',
            name='id_images',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='model_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
