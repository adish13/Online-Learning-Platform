# Generated by Django 3.2.8 on 2021-11-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0004_auto_20211124_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
