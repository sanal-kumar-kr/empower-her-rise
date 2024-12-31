# Generated by Django 5.0.4 on 2024-05-30 01:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_App', '0005_inbox'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inbox',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='inbox',
            name='message',
        ),
        migrations.RemoveField(
            model_name='inbox',
            name='reciever',
        ),
        migrations.RemoveField(
            model_name='inbox',
            name='sender',
        ),
        migrations.AddField(
            model_name='inbox',
            name='gpid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orgWEWRE_id', to='Admin_App.talentgroup'),
        ),
        migrations.AddField(
            model_name='inbox',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_WDEWQperson', to=settings.AUTH_USER_MODEL),
        ),
    ]