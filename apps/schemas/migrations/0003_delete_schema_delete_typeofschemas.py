# Generated by Django 4.1.6 on 2023-02-05 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0002_schema'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Schema',
        ),
        migrations.DeleteModel(
            name='TypeOfSchemas',
        ),
    ]