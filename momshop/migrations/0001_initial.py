# Generated by Django 2.0.4 on 2018-05-04 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=100, verbose_name='Название')),
                ('image', models.ImageField(upload_to='carousel/', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('image', models.ImageField(default='Категория', upload_to='category', verbose_name='Изображение категории')),
            ],
        ),
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='products', verbose_name='Изображение')),
                ('consist', models.CharField(default='', max_length=200, verbose_name='Состав')),
                ('availability', models.BooleanField(default=True, verbose_name='Доступен на сайте')),
                ('avalability_type', models.CharField(choices=[('a', 'В наличии'), ('o', 'Под заказ')], default='a', max_length=10, verbose_name='Наличие')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('models_height', models.PositiveIntegerField(default=0, verbose_name='Высота модели')),
                ('creation', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='momshop.Category', verbose_name='Категория')),
                ('tags', models.ManyToManyField(to='momshop.Keywords', verbose_name='Ключевые слова')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
