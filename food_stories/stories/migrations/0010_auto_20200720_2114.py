# Generated by Django 3.0.7 on 2020-07-20 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0009_auto_20200720_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='min_read_time',
            field=models.PositiveIntegerField(null=True, verbose_name='Min read time'),
        ),
    ]