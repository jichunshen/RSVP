# Generated by Django 2.0.2 on 2018-02-05 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0011_textquestion_vendor_cansee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textanswer',
            name='answer',
            field=models.TextField(max_length=1000),
        ),
    ]
