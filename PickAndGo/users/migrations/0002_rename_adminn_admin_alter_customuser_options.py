# Generated by Django 4.2.16 on 2024-09-06 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Adminn',
            new_name='Admin',
        ),
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': [('can_view_customuser', 'Can view CustomUser'), ('can_create_owner', 'Can create owner')]},
        ),
    ]