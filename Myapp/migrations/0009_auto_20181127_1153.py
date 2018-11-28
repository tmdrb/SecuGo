# Generated by Django 2.1 on 2018-11-27 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0008_comparesource'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comparesource',
            name='java',
        ),
        migrations.RemoveField(
            model_name='comparesource',
            name='javascript',
        ),
        migrations.RemoveField(
            model_name='comparesource',
            name='php',
        ),
        migrations.RemoveField(
            model_name='comparesource',
            name='python',
        ),
        migrations.AddField(
            model_name='comparesource',
            name='entities',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]