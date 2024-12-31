# Generated by Django 5.0.4 on 2024-05-29 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('description', models.CharField(default='', max_length=50)),
                ('Fees', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='hostals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostal_name', models.CharField(default='', max_length=50)),
                ('location', models.CharField(default='', max_length=50)),
                ('address', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firm_name', models.CharField(default='', max_length=50)),
                ('title', models.CharField(default='', max_length=50)),
                ('description', models.CharField(default='', max_length=50)),
                ('qualification', models.TextField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='awarnessclasses',
        ),
    ]
