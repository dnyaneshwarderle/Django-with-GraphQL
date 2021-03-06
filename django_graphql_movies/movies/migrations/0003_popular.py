# Generated by Django 2.1.3 on 2020-07-01 11:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_delete_popular'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_ids', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=10)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
