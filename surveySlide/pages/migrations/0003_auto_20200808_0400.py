# Generated by Django 3.0.8 on 2020-08-07 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200808_0346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='gender_filter1',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='gender_filter2',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='grade_filter1',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='grade_filter2',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='grade_filter3',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='grade_filter4',
        ),
        migrations.AddField(
            model_name='survey',
            name='gender_filter',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='grade_filter',
            field=models.IntegerField(null=True),
        ),
    ]
