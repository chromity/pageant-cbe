# Generated by Django 2.1 on 2018-08-12 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0006_auto_20180812_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='RankSix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='candidates.Candidate')),
            ],
        ),
        migrations.AlterField(
            model_name='pageantresult',
            name='candidate',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='candidates.RankSix'),
        ),
    ]