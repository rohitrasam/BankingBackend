# Generated by Django 4.0.6 on 2022-07-13 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendAPI', '0011_alter_accounts_id_alter_balance_id_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='id',
            field=models.BigIntegerField(auto_created=True, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='balance',
            name='id',
            field=models.BigIntegerField(auto_created=True, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigIntegerField(auto_created=True, editable=False, primary_key=True, serialize=False),
        ),
    ]
