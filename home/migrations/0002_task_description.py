# Generated by Django 3.2 on 2021-04-20 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default='description'),
            preserve_default=False,
        ),
    ]