# Generated by Django 2.0.2 on 2018-02-05 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_auto_20180205_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='textquestion',
            name='vendor_cansee',
            field=models.BooleanField(default=False),
        ),
    ]
