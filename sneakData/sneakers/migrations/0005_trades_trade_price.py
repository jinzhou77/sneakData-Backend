# Generated by Django 3.2.5 on 2021-07-11 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0004_trades'),
    ]

    operations = [
        migrations.AddField(
            model_name='trades',
            name='trade_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]
