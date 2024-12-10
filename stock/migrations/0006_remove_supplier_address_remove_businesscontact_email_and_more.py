# Generated by Django 5.1.2 on 2024-10-16 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_alter_address_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='address',
        ),
        migrations.RemoveField(
            model_name='businesscontact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='businesscontact',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='document',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='user',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='BusinessContact',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
    ]
