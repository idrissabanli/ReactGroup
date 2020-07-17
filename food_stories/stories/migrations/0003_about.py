# Generated by Django 3.0.7 on 2020-07-10 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_story'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone Number')),
                ('location', models.CharField(max_length=50, verbose_name='Location')),
                ('email', models.EmailField(max_length=30, verbose_name='Email')),
                ('description', models.TextField(verbose_name='Description')),
                ('daily_visitors', models.PositiveIntegerField(verbose_name='Daile Visitors')),
                ('facebook_page_url', models.URLField(verbose_name='Facebook page url')),
                ('instagram_page_url', models.URLField(verbose_name='Instagram page url')),
                ('twitter_page_url', models.URLField(verbose_name='Instagram page url')),
            ],
            options={
                'verbose_name': 'About Site Information',
                'verbose_name_plural': 'About Site Informations',
            },
        ),
    ]