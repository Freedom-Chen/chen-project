# Generated by Django 2.2.1 on 2019-07-12 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_remove_comment_auth'),
        ('xadmin', '0003_auto_20160715_0100'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('blog', '0003_auto_20190712_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='BlogUser',
        ),
    ]
