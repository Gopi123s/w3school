# Generated by Django 4.1.3 on 2022-12-28 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course_name',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('cat', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=3000)),
                ('url', models.CharField(max_length=1000)),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='course_pic/')),
            ],
        ),
        migrations.CreateModel(
            name='Add_course_part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_title', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=30000000)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='course_part_pic/')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elearns.course_name')),
            ],
        ),
    ]