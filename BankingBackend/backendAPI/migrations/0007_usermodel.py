# Generated by Django 4.0.6 on 2022-07-11 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0006_alter_accounts_account_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
