# Generated by Django 2.0.2 on 2018-02-07 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0022_choice_multianswer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='multianswer',
        ),
        migrations.AddField(
            model_name='choice',
            name='answer_question',
            field=models.ManyToManyField(related_name='answer_question', to='event.TextQuestion'),
        ),
    ]
