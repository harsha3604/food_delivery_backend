# Generated by Django 4.1.5 on 2023-04-20 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_app_menu', '0005_cartitem_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='total_price',
            new_name='total_cost',
        ),
    ]
