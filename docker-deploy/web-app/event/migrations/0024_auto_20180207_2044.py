# Generated by Django 2.0.2 on 2018-02-07 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0023_auto_20180207_2000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='answer_question',
        ),
        migrations.RemoveField(
            model_name='multianswer',
            name='user_answermulti',
        ),
        migrations.AddField(
            model_name='multianswer',
            name='selected_choice',
            field=models.ManyToManyField(related_name='selected_choice', to='event.Choice'),
        ),
    ]
