# Generated by Django 2.2 on 2021-08-13 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_review_fish_reviewed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='fish_reviewed',
        ),
        migrations.AddField(
            model_name='review',
            name='fish_reviewed',
            field=models.ManyToManyField(null=True, related_name='fish_reviews', to='main.Fish'),
        ),
        migrations.RemoveField(
            model_name='review',
            name='lure_reviewed',
        ),
        migrations.AddField(
            model_name='review',
            name='lure_reviewed',
            field=models.ManyToManyField(null=True, related_name='lure_reviews', to='main.Lure'),
        ),
    ]