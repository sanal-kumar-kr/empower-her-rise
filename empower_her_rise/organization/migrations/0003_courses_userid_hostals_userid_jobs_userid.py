# Generated by Django 5.0.4 on 2024-05-29 01:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_courses_hostals_jobs_delete_awarnessclasses'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oiopetertyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hostals',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oirewop', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='jobs',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oweriop', to=settings.AUTH_USER_MODEL),
        ),
    ]