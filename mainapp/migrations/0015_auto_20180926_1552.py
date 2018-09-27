# Generated by Django 2.1 on 2018-09-26 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20180925_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('WordName', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='wordsall',
            name='WordEachName',
        ),
        migrations.RemoveField(
            model_name='findwords',
            name='id',
        ),
        migrations.AddField(
            model_name='collectors',
            name='CollectUser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.MyUser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='findwords',
            name='FindAuthorName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Author'),
        ),
        migrations.AlterField(
            model_name='findwords',
            name='FindWordsId',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='WordsAll',
        ),
        migrations.DeleteModel(
            name='WordsList',
        ),
        migrations.AddField(
            model_name='findwords',
            name='FindWordName',
            field=models.ForeignKey(default=1, max_length=50, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Words'),
            preserve_default=False,
        ),
    ]
