# Generated by Django 5.0.4 on 2024-06-15 07:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0012_delete_feedback'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(null=True)),
                ('ratings', models.IntegerField(null=True)),
                ('hostalid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oirtryguhijofrewgfrewuketerwtwop', to='organization.hostals')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oirtryguhijoketerwtwop', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
