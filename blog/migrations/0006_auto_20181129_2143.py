# Generated by Django 2.1.2 on 2018-11-29 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181129_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(allow_unicode=True),
        ),
    ]
