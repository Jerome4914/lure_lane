# Generated by Django 2.2 on 2021-08-12 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210812_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='fish',
            name='fish_breed',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
