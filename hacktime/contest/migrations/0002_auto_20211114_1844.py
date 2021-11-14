# Generated by Django 3.1 on 2021-11-14 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parentContest',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='contest.contest'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='date',
            field=models.DateField(default='2021-12-12'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='daysLeftToRegister',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contest',
            name='isRated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contest',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
