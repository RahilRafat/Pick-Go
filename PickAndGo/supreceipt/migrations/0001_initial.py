# Generated by Django 4.2.16 on 2024-09-06 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food', '0002_initial'),
        ('sizes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supreceipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('totalsupprice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('food_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.food')),
                ('size_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sizes.size')),
            ],
        ),
    ]
