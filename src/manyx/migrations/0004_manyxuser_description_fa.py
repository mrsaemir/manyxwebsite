# Generated by Django 2.1.2 on 2018-11-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manyx', '0003_manyxuser_full_name_fa'),
    ]

    operations = [
        migrations.AddField(
            model_name='manyxuser',
            name='description_fa',
            field=models.TextField(blank=True, null=True),
        ),
    ]
