# Generated by Django 3.0.8 on 2020-08-28 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200828_2328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='gainedpoint',
            new_name='gained_point',
        ),
    ]