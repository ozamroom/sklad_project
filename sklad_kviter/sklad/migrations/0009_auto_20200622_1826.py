# Generated by Django 3.0.6 on 2020-06-22 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sklad', '0008_auto_20200618_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail_in_products',
            name='detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='sklad.List_details', verbose_name='детали'),
        ),
    ]
