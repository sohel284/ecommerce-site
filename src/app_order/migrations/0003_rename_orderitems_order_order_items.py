# Generated by Django 3.2.3 on 2021-06-02 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_order', '0002_rename_orederitems_order_orderitems'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orderitems',
            new_name='order_items',
        ),
    ]
