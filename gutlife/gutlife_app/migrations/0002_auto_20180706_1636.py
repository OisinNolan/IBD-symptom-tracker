# Generated by Django 2.0.2 on 2018-07-06 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gutlife_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmlog',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bmlog',
            name='datecode',
            field=models.DateField(),
        ),
    ]
