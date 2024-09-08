# Generated by Django 4.2.16 on 2024-09-06 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pickup', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickup',
            name='owner_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickupsowner', to='users.owner'),
        ),
        migrations.AddField(
            model_name='pickup',
            name='user_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickupsusername', to='users.customuser'),
        ),
    ]