# Generated by Django 4.1.7 on 2023-03-06 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crud_student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('mobile_no', models.IntegerField()),
                ('gender', models.CharField(max_length=2)),
            ],
        ),
    ]
