# Generated by Django 3.0.7 on 2020-08-07 06:28

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(blank=True, max_length=20, null=True)),
                ('major', models.CharField(blank=True, max_length=20, null=True)),
                ('point', models.IntegerField(default=1000)),
                ('changedpoint', models.IntegerField(default=0)),
                ('chargedpoint', models.IntegerField(default=0)),
                ('gainedpoint', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
