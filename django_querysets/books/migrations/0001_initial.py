# Generated by Django 3.0.7 on 2020-06-17 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Tam Adı')),
                ('image', models.ImageField(upload_to='author_images', verbose_name='Şəkil')),
                ('gender', models.IntegerField(choices=[(1, 'Kişi'), (2, 'Qadın')], verbose_name='Cins')),
                ('date_of_birthday', models.DateField(blank=True, null=True, verbose_name='Doğum günü')),
                ('nationality', models.CharField(blank=True, max_length=50, null=True, verbose_name='Milliyəti')),
                ('info', models.TextField(blank=True, null=True, verbose_name='Haqqında Məlumat')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlığı')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Başlığı')),
                ('description', models.TextField(verbose_name='Məzmunu')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Qiyməti')),
                ('page_count', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Səhifə sayı')),
                ('cover_image', models.ImageField(upload_to='book_images', verbose_name='Şəkil')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.Author')),
                ('category', models.ManyToManyField(related_name='books', to='books.Category')),
            ],
        ),
    ]