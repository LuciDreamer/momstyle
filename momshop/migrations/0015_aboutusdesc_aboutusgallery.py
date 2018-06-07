# Generated by Django 2.0.5 on 2018-05-30 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('momshop', '0014_auto_20180523_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='', verbose_name='Описание на странице "О нас"')),
            ],
        ),
        migrations.CreateModel(
            name='AboutUsGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_us', verbose_name='Фото галереи')),
                ('description', models.CharField(max_length=500, verbose_name='Подпись к фото')),
            ],
            options={
                'verbose_name': 'Фотография галереи',
                'verbose_name_plural': 'Фотографии галереи',
            },
        ),
    ]
