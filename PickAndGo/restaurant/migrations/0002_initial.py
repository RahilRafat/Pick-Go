# Generated by Django 4.2.16 on 2024-09-06 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='admin_fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.adminn'),
        ),
    ]