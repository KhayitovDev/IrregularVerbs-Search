# Generated by Django 4.2 on 2023-04-19 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word_search', '0002_rename_words_word'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='example',
        ),
        migrations.AddField(
            model_name='word',
            name='example_first',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='word',
            name='example_second',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='word',
            name='example_third',
            field=models.TextField(blank=True),
        ),
    ]
