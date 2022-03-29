# Generated by Django 4.0.3 on 2022-03-27 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionpool', '0009_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_department',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_semester',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_subject',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='department',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='semester',
        ),
        migrations.DeleteModel(
            name='department',
        ),
        migrations.DeleteModel(
            name='question',
        ),
        migrations.DeleteModel(
            name='semester',
        ),
        migrations.DeleteModel(
            name='subject',
        ),
    ]
