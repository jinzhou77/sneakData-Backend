# Generated by Django 3.2.4 on 2021-07-24 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0013_auto_20210723_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebaytrades',
            name='ebay_trade_url',
            field=models.CharField(default='url not exist', max_length=255),
            preserve_default=False,
        ),
    ]
