# Generated by Django 3.0.7 on 2020-06-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default=1, upload_to='media/recipes/'),
            preserve_default=False,
        ),
    ]
