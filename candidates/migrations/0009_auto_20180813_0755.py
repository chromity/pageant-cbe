# Generated by Django 2.1 on 2018-08-13 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0008_auto_20180813_0743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pageantnight',
            name='votes',
        ),
        migrations.AddField(
            model_name='pageantnight',
            name='formal_attire_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pageantnight',
            name='old_street_fashion_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pageantnight',
            name='uniform_votes',
            field=models.IntegerField(default=0),
        ),
    ]