# Generated by Django 4.0.6 on 2022-07-11 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0002_remove_balance_account_no_balance_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='account_type',
            field=models.PositiveIntegerField(choices=[('Savings', 'Savings'), ('Current', 'Current')], default='Savings'),
        ),
    ]
