# Generated by Django 3.2.5 on 2021-07-12 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0011_alter_trades_trade_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trades',
            old_name='trade_date',
            new_name='trade_date_time',
        ),
        migrations.RemoveField(
            model_name='trades',
            name='trade_time',
        ),
    ]