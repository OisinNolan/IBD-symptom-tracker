# Generated by Django 2.0.2 on 2018-07-07 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gutlife_app', '0005_auto_20180707_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmlog',
            name='time',
            field=models.CharField(max_length=5),
        ),
    ]
