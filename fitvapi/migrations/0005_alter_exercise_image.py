# Generated by Django 4.0.3 on 2022-03-22 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitvapi', '0004_exercise_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='image',
            field=models.URLField(),
        ),
    ]
