# Generated by Django 4.2.16 on 2024-09-09 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supreceipt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supreceipt',
            name='totalsupprice',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]