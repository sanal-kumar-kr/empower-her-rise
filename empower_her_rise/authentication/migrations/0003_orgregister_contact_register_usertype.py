# Generated by Django 4.2.4 on 2024-05-06 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_dhoregister_orgregister_policeofficerregister_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgregister',
            name='contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='usertype',
            field=models.CharField(default='admin', max_length=50),
        ),
    ]
