# Generated by Django 4.0.3 on 2022-03-28 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionpool', '0013_remove_question_question_course_and_more'),
        ('authentication', '0004_rename_department_name_department_department_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='subject',
        ),
    ]
