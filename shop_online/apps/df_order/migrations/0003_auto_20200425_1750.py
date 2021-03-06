# Generated by Django 2.0.7 on 2020-04-25 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('df_order', '0002_auto_20200307_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetailinfo',
            name='count',
            field=models.IntegerField(verbose_name='商品数'),
        ),
        migrations.AlterField(
            model_name='orderdetailinfo',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_goods.GoodsInfo', verbose_name='商品'),
        ),
        migrations.AlterField(
            model_name='orderdetailinfo',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='商品价格'),
        ),
    ]
