# Generated by Django 2.2 on 2021-08-12 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210812_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lure',
            name='this_fish',
            field=models.ManyToManyField(related_name='this_fish', to='main.Fish'),
        ),
    ]
