# Generated by Django 3.1.6 on 2021-02-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharing', '0005_item_clothing_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.FloatField(default=7.5, verbose_name='size'),
            preserve_default=False,
        ),
    ]
