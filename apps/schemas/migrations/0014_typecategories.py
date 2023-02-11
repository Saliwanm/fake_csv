# Generated by Django 4.1.6 on 2023-02-07 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0013_schema_column_separator_schema_string_character'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('cut_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schemas.schema')),
            ],
        ),
    ]
