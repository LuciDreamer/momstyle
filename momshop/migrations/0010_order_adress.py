# Generated by Django 2.0.5 on 2018-05-16 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('momshop', '0009_auto_20180516_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='adress',
            field=models.CharField(default='', max_length=500, verbose_name='Адресс'),
        ),
    ]