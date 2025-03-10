# Generated by Django 5.1.2 on 2024-11-01 01:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0010_alter_product_base_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='stock.product', verbose_name='Produto'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='stock.supplier', verbose_name='Fornecedor'),
        ),
        migrations.AlterField(
            model_name='stockentry',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stock_entries', to='stock.product', verbose_name='Produto'),
        ),
        migrations.AlterField(
            model_name='stockentry',
            name='stock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stock_entries', to='stock.stock', verbose_name='Estoque'),
        ),
        migrations.AlterField(
            model_name='stockentry',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stock_entries', to='stock.supplier', verbose_name='Fornecedor'),
        ),
        migrations.AlterField(
            model_name='stockexit',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stock_exits', to='stock.product', verbose_name='Produto'),
        ),
        migrations.AlterField(
            model_name='stockexit',
            name='stock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stock_exits', to='stock.stock', verbose_name='Estoque'),
        ),
    ]
