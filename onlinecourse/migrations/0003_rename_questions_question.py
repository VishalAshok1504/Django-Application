# Generated by Django 4.2.7 on 2023-11-27 19:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("onlinecourse", "0002_choice_submission_questions_choice_course"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Questions",
            new_name="Question",
        ),
    ]
