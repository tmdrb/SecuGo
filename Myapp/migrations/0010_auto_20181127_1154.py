# Generated by Django 2.1 on 2018-11-27 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0009_auto_20181127_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comparesource',
            old_name='entities',
            new_name='lang',
        ),
        migrations.AddField(
            model_name='comparesource',
            name='source',
            field=models.TextField(blank=True, null=True),
        ),
    ]
