# Generated by Django 3.2.3 on 2021-06-02 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_order', '0003_rename_orderitems_order_order_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
