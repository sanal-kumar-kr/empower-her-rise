# Generated by Django 5.0.4 on 2024-05-28 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_App', '0003_alter_talentgroup_description_classes_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classes',
            name='class_category',
        ),
    ]
