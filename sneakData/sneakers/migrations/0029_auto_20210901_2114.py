# Generated by Django 3.2.4 on 2021-09-02 02:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sneakers', '0028_stockx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analyze',
            fields=[
                ('analyze_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('analyze_target_date', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('average_price', models.CharField(max_length=255, null=True)),
                ('high_price', models.CharField(max_length=255, null=True)),
                ('low_price', models.CharField(max_length=255, null=True)),
                ('number_of_trades', models.IntegerField()),
                ('publish_date', models.CharField(max_length=255)),
                ('platform', models.CharField(max_length=255)),
                ('sneaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sneakers.detail')),
            ],
        ),
        migrations.DeleteModel(
            name='Stockx',
        ),
    ]
