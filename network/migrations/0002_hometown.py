# Generated by Django 4.1.2 on 2023-01-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hometown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hometown', models.CharField(max_length=100)),
            ],
        ),
    ]