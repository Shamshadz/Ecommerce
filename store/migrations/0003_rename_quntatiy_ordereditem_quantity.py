# Generated by Django 4.1 on 2022-09-04 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordereditem',
            old_name='quntatiy',
            new_name='quantity',
        ),
    ]
