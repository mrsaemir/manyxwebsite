# Generated by Django 2.1.2 on 2018-10-25 06:25

from django.db import migrations
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manyxproject',
            name='creation_date',
            field=django_jalali.db.models.jDateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]