# Generated by Django 4.2.5 on 2023-11-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_billsequence_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='product_ids',
            field=models.ManyToManyField(blank=True, to='base.product'),
        ),
    ]
