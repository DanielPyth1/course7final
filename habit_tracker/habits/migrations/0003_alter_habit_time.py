# Generated by Django 5.1.3 on 2024-11-23 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0002_habit_reminder_time_alter_habit_action"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="time",
            field=models.TimeField(
                blank=True, null=True, verbose_name="Время выполнения"
            ),
        ),
    ]
