# Generated by Django 4.0.6 on 2022-07-12 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0008_user_soft_delete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='soft_delete',
            new_name='is_deleted',
        ),
    ]
