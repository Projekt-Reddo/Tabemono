# Generated by Django 3.1 on 2020-12-23 09:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='orderfood',
            name='food_id',
        ),
        migrations.RemoveField(
            model_name='orderfood',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='food',
        ),
        migrations.RemoveField(
            model_name='shipping',
            name='order',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='dateOfBirth',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='is_shipper',
        ),
        migrations.DeleteModel(
            name='Food',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderFood',
        ),
        migrations.DeleteModel(
            name='Shipping',
        ),
    ]
