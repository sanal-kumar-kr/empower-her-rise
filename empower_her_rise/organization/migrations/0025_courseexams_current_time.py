# Generated by Django 5.0.4 on 2024-06-15 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0024_remove_courseexams_current_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseexams',
            name='current_time',
            field=models.TimeField(null=True),
        ),
    ]