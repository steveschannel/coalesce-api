# Generated by Django 3.1.6 on 2021-02-12 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationdata',
            name='latitude',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='locationdata',
            name='longitude',
            field=models.FloatField(default=None, null=True),
        ),
    ]
