# Generated by Django 3.2.8 on 2021-11-27 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0003_progressinstructor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default='', upload_to='')),
            ],
        ),
    ]