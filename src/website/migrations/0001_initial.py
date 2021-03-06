# Generated by Django 2.1.2 on 2018-11-04 11:19

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManyxProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('title', models.CharField(max_length=30, unique=True)),
                ('snapshot', models.ImageField(null=True, upload_to='snapshots')),
                ('start_date', django_jalali.db.models.jDateField()),
                ('end_date', django_jalali.db.models.jDateField(null=True)),
                ('live_url', models.URLField(blank=True, null=True)),
                ('git_repository_url', models.URLField(blank=True, null=True)),
                ('estimated_hours', models.PositiveIntegerField(null=True)),
                ('team_members', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
        ),
    ]
