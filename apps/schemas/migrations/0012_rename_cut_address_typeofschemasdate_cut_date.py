# Generated by Django 4.1.6 on 2023-02-05 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0011_alter_columnseparator_column_separator_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='typeofschemasdate',
            old_name='cut_address',
            new_name='cut_date',
        ),
    ]
