# Generated by Django 2.0.5 on 2018-05-16 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('momshop', '0008_orderitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='momshop.Products', verbose_name='Товар'),
        ),
    ]
