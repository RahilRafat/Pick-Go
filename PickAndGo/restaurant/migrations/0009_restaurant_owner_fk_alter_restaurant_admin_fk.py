# Generated by Django 4.2.16 on 2024-09-09 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0008_alter_restaurant_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='owner_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurants_as_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='admin_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurants_as_admin', to=settings.AUTH_USER_MODEL),
        ),
    ]