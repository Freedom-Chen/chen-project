# Generated by Django 2.2.1 on 2019-07-18 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zbest', '0007_auto_20190718_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.BooleanField(default=1),
        ),
    ]
