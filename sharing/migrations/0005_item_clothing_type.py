# Generated by Django 3.1.6 on 2021-02-12 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharing', '0004_auto_20210212_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='clothing_type',
            field=models.CharField(choices=[('M', 'Male presenting clothing'), ('F', 'Female presenting clothing'), ('A', 'Any')], default='A', max_length=1, verbose_name='clothing type'),
        ),
    ]
