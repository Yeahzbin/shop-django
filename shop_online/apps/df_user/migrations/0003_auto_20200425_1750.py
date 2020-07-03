# Generated by Django 2.0.7 on 2020-04-25 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0002_auto_20200307_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsbrowser',
            name='good',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_goods.GoodsInfo', verbose_name='商品ID'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ushou',
            field=models.CharField(default='', max_length=20, verbose_name='收货地址'),
        ),
    ]