# Generated by Django 3.0.7 on 2020-07-20 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0008_auto_20200720_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='min_read_time',
            field=models.PositiveIntegerField(editable=False, null=True, verbose_name='Min read time'),
        ),
    ]
