# Generated by Django 2.2 on 2021-08-12 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_fish_fish_breed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='all_fish',
            field=models.CharField(choices=[('CR', 'crappie'), ('BS', 'bass'), ('TR', 'trout'), ('WL', 'walleye'), ('ST', 'striper'), ('MU', 'muskie'), ('PI', 'pike'), ('SA', 'salmon')], max_length=2),
        ),
    ]