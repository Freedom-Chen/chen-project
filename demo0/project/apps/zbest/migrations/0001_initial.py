# Generated by Django 2.2.1 on 2019-07-17 01:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('portrait', models.ImageField(upload_to=' portrait')),
                ('email', models.EmailField(default='123@a.com', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('desc', models.TextField()),
                ('price', models.FloatField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('showimg', models.ImageField(upload_to='showimg')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zbest.Category')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zbest.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.UUIDField(default=uuid.uuid4, help_text='app uuid', verbose_name='app uuid')),
                ('total', models.FloatField()),
                ('state', models.CharField(default='待支付', max_length=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zbest.Account')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zbest.Account')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zbest.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zbest.Goods')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zbest.Order')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='goodimg')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zbest.Goods')),
            ],
        ),
    ]
