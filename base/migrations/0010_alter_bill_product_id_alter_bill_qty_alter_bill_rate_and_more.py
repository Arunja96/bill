# Generated by Django 4.2.5 on 2023-11-13 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_bill_product_id_bill_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='product_id',
            field=models.ManyToManyField(blank=True, null=True, to='base.product'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='qty',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='rate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='si_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='total_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
