# Generated by Django 3.2.5 on 2021-07-03 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=200)),
                ('mfg_date', models.DateTimeField(verbose_name='date manufactured')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='assets.producttype')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='assets.version')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=200)),
                ('mfg_date', models.DateTimeField(verbose_name='date manufactured')),
                ('module_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='assets.moduletype')),
                ('unit', models.ManyToManyField(blank=True, to='assets.Unit')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='assets.version')),
            ],
        ),
    ]
