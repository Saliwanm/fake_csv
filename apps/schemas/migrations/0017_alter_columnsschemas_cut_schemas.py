# Generated by Django 4.1.6 on 2023-02-10 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0016_columnsschemas_name_columnsschemas_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='columnsschemas',
            name='cut_schemas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='schemas.schema'),
        ),
    ]
