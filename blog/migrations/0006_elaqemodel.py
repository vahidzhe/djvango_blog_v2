# Generated by Django 3.1.5 on 2022-08-08 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20220808_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElaqeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('ad_soyad', models.CharField(max_length=150)),
                ('yazi', models.TextField()),
                ('yaranma_tarixi', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Əlaqə',
                'verbose_name_plural': 'Əlaqə',
                'db_table': 'elaqe',
            },
        ),
    ]
