# Generated by Django 2.1 on 2018-08-12 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0004_auto_20180811_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='formalattiretotal',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='oldstreetfashionattiretotal',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pageantnight',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pageantproper',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pageantresult',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='prepageanttotal',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionandanswertotal',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='uniformattiretotal',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
