# Generated by Django 2.0.2 on 2018-02-07 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0018_textquestion_is_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.TextQuestion')),
                ('user_answermulti', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_answermulti', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='userchoose',
            field=models.ManyToManyField(related_name='userchoose', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='choice',
            name='multianswer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='multianswer', to='event.MultiAnswer'),
        ),
    ]
