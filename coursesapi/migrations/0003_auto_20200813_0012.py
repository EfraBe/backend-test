# Generated by Django 3.1 on 2020-08-13 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursesapi', '0002_courses_lessions_questions'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Courses',
            new_name='Course',
        ),
        migrations.RenameModel(
            old_name='Lessions',
            new_name='Lession',
        ),
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
    ]
