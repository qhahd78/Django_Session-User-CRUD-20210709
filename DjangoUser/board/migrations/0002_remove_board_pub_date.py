# Generated by Django 3.1.7 on 2021-07-08 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='pub_date',
        ),
    ]
