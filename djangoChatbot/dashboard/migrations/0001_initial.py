# Generated by Django 3.2.7 on 2022-06-13 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookTutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('tutorname', models.CharField(max_length=100)),
                ('studentname', models.CharField(max_length=100)),
                ('dateofthesession', models.CharField(max_length=100)),
                ('starttime', models.CharField(max_length=100)),
                ('totalduration', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('expectation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('qual', models.CharField(max_length=100)),
                ('pnumber', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=100)),
                ('Specialization', models.CharField(max_length=500)),
                ('display_name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('study', models.CharField(max_length=100)),
                ('YOP', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=50)),
                ('CGPA', models.CharField(max_length=50)),
                ('College', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('Interest', models.CharField(max_length=500)),
            ],
        ),
    ]
