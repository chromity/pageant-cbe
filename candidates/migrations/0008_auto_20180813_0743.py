# Generated by Django 2.1 on 2018-08-13 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0007_auto_20180812_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pageantproper',
            name='votes',
        ),
        migrations.AddField(
            model_name='pageantproper',
            name='formal_attire_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pageantproper',
            name='old_street_fashion_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pageantproper',
            name='uniform_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='questionandanswertotal',
            name='candidate',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='candidates.RankSix'),
        ),
    ]