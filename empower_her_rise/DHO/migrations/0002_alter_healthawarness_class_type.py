# Generated by Django 5.0.4 on 2024-05-26 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DHO', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthawarness',
            name='class_type',
            field=models.CharField(choices=[('', 'Select'), ('online', 'online'), ('offline', 'offline')], default='', max_length=50),
        ),
    ]