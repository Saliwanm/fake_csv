# Generated by Django 4.1.6 on 2023-02-07 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0015_remove_typecategories_cut_type_columnsschemas'),
    ]

    operations = [
        migrations.AddField(
            model_name='columnsschemas',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='columnsschemas',
            name='order',
            field=models.IntegerField(default=0, null=True),
        ),
    ]