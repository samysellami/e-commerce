# Generated by Django 3.2.6 on 2021-08-28 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_descrtption_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingadress',
            old_name='adress',
            new_name='address',
        ),
    ]
