# Generated by Django 2.1 on 2018-09-25 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20180925_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='copybookall',
            name='id',
        ),
        migrations.AddField(
            model_name='copybookall',
            name='CopyBookEachId',
            field=models.CharField(default=1, max_length=100, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
