# Generated by Django 4.0.6 on 2022-07-12 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0007_usermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='soft_delete',
            field=models.BooleanField(default=False),
        ),
    ]
