# Generated by Django 3.2.5 on 2021-07-12 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0005_trades_trade_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='trades',
            name='trade_time',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='trades',
            name='trade_size',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]
