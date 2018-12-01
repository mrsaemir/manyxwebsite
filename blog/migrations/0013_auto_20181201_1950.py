# Generated by Django 2.1.2 on 2018-12-01 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_blog_publication_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='dislikes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blog',
            name='reports',
            field=models.PositiveIntegerField(default=0),
        ),
    ]