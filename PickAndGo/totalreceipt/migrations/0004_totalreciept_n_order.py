# Generated by Django 4.2.16 on 2024-09-08 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totalreceipt', '0003_alter_totalreciept_total_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalreciept',
            name='n_order',
            field=models.IntegerField(default=1),
        ),
    ]
