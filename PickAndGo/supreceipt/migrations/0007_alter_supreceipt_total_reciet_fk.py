# Generated by Django 4.2.16 on 2024-09-09 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('totalreceipt', '0008_alter_totalreciept_total_receipt'),
        ('supreceipt', '0006_alter_supreceipt_total_reciet_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supreceipt',
            name='total_reciet_fk',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='totalreceipt.totalreciept'),
        ),
    ]
