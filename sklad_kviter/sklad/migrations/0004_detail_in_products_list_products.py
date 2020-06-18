# Generated by Django 3.0.6 on 2020-06-17 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sklad', '0003_auto_20200617_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail_in_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_count', models.IntegerField()),
                ('slug', models.SlugField(unique=True)),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='sklad.List_details', verbose_name='детали')),
            ],
        ),
        migrations.CreateModel(
            name='List_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
                ('slug', models.SlugField(unique=True)),
                ('obj_details', models.ManyToManyField(blank=True, to='sklad.Detail_in_products', verbose_name='детали')),
            ],
        ),
    ]
