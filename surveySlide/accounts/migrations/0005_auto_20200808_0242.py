# Generated by Django 3.0.8 on 2020-08-07 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
