# Generated by Django 3.1.5 on 2022-07-26 12:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_meqalemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meqalemodel',
            name='yazi',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
