# Generated by Django 4.0.6 on 2022-07-11 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0004_alter_accounts_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='account_type',
            field=models.CharField(choices=[('Savings', 'Savings'), ('Current', 'Current')], default='Savings', max_length=20, null=True),
        ),
    ]
