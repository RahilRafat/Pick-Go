# Generated by Django 4.2.16 on 2024-09-09 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totalreceipt', '0004_totalreciept_n_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalreciept',
            name='total_receipt',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]
