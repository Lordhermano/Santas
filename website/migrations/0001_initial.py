# Generated by Django 5.1.4 on 2025-01-07 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Createaccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('account', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=400)),
                ('date_of_birth', models.DateField(max_length=200)),
            ],
        ),
    ]