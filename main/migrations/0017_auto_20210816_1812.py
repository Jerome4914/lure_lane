# Generated by Django 2.2 on 2021-08-16 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_remove_fish_all_fish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fish',
            name='location',
        ),
        migrations.AddField(
            model_name='fish',
            name='this_fish',
            field=models.CharField(choices=[('Crappie', 'Crappie'), ('Bass', 'Bass'), ('Trout', 'Trout'), ('Striper', 'Striper'), ('Musky', 'Musky'), ('Walleye', 'Walleye'), ('Pike', 'Pike'), ('Salmon', 'Salmon')], default='coding', max_length=50),
        ),
    ]
