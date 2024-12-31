# Generated by Django 5.0.4 on 2024-05-31 01:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_App', '0010_alter_classes_userid_booking'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(null=True)),
                ('reply', models.TextField(null=True)),
                ('status', models.IntegerField(default=0, null=True)),
                ('classid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adssigfetwtetrterrtewrthjkghjd', to='Admin_App.classes')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sdassigfhdfhydfhetjkadgtsdgghjd', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
