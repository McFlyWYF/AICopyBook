# Generated by Django 2.1 on 2018-09-24 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_copybook_contentimgurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='copybook',
            name='contentImgUrl',
        ),
    ]
