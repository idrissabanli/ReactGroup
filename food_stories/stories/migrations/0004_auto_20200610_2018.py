# Generated by Django 3.0.7 on 2020-06-10 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20200610_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.IntegerField(choices=[(1, 'Dessert'), (2, 'Food')], default=2),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='short_description',
            field=models.TextField(help_text='bu reseptler siyahisinda cixacaq metindir', max_length=1000),
        ),
        migrations.AlterModelTable(
            name='recipe',
            table='recipes',
        ),
    ]
