# Generated by Django 3.1.5 on 2021-01-23 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20210123_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationdata',
            name='city',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='locationdata',
            name='state',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
    ]