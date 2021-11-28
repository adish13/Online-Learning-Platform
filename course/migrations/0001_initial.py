# Generated by Django 3.2.8 on 2021-11-28 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instructor', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isTA', models.BooleanField(default=False)),
                ('grade', models.CharField(blank=True, max_length=100, null=True)),
                ('marks', models.FloatField(default=0, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructor.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll_no', models.CharField(max_length=100)),
                ('course_list', models.ManyToManyField(blank=True, through='course.Membership', to='instructor.Course')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_resource', models.FileField(default='', upload_to='')),
                ('title', models.CharField(max_length=100)),
                ('post_time', models.DateTimeField(blank=True, null=True)),
                ('course', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='instructor.course')),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('assignments', models.ManyToManyField(to='instructor.Assignment')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructor.course')),
                ('resources', models.ManyToManyField(to='course.Resources')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.student')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('content', models.TextField(max_length=500)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('course', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='instructor.course')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('time', models.CharField(max_length=100)),
                ('course', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='instructor.course')),
                ('sender', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.student'),
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_content', models.TextField(max_length=500)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together={('student', 'course')},
        ),
    ]
