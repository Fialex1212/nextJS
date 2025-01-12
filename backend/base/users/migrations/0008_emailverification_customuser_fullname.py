# Generated by Django 5.1 on 2024-12-22 16:15

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_customuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('code', models.CharField(max_length=6)),
                ('expires_at', models.DateTimeField(default=users.models.calculate_expires_at)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='fullname',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
