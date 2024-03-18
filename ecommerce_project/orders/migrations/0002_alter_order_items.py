# Generated by Django 4.0.2 on 2024-03-18 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='orders.OrderedItem', to='cart.CartItem'),
        ),
    ]