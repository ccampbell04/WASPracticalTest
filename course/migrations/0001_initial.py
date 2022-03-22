# Generated by Django 4.0.3 on 2022-03-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('start_date', models.DateField()),
                ('description', models.CharField(max_length=1028)),
            ],
        ),
    ]
