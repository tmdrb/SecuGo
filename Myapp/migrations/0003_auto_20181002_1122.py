# Generated by Django 2.1 on 2018-10-02 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_auto_20181002_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='categories',
            field=models.CharField(max_length=255),
        ),
    ]
