# Generated by Django 5.0.4 on 2024-05-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DHO', '0002_alter_healthawarness_class_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='healthawarness',
        ),
        migrations.AlterField(
            model_name='schemas',
            name='required',
            field=models.TextField(default=''),
        ),
    ]