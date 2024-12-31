# Generated by Django 5.0.4 on 2024-06-15 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0020_delete_courseexams'),
    ]

    operations = [
        migrations.CreateModel(
            name='courseexams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default='', max_length=250)),
                ('courseid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='yyrrr', to='organization.courses')),
            ],
        ),
    ]
