# Generated by Django 2.2.1 on 2019-07-19 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zbest', '0008_auto_20190718_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordergoods',
            name='state',
            field=models.BooleanField(default=1),
        ),
    ]
