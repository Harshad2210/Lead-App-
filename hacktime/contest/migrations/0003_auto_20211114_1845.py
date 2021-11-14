# Generated by Django 3.1 on 2021-11-14 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contest', '0002_auto_20211114_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
