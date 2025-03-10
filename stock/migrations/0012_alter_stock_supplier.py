# Generated by Django 5.1.2 on 2024-11-02 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0011_alter_stock_product_alter_stock_supplier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='stock.supplier', verbose_name='Fornecedor'),
        ),
    ]
