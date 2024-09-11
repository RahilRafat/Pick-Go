# Generated by Django 4.2.16 on 2024-09-10 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=13)),
                ('address', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='./media/')),
                ('admin_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurants_as_admin', to=settings.AUTH_USER_MODEL)),
                ('owner_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurants_as_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
