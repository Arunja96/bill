# Generated by Django 4.2.5 on 2023-11-12 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('si_no', models.IntegerField()),
                ('qty', models.FloatField()),
                ('rate', models.FloatField()),
                ('total', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.product')),
            ],
        ),
    ]
