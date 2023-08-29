# Generated by Django 4.0.4 on 2022-11-29 16:06

from django.db import migrations, models
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0033_alter_glycerolstock_qr_id_alter_plasmid_qr_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glycerolstock',
            name='qr_id',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, default='JP3xcESxmfEbWytVwy2DxH', editable=False, max_length=22),
        ),
        migrations.AlterField(
            model_name='plasmid',
            name='idx',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='plasmid',
            name='qr_id',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, default='L8wp9dazhBgUZeZjU4GTns', editable=False, max_length=22),
        ),
        migrations.AlterField(
            model_name='primer',
            name='qr_id',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, default='3Js7QDRBaFEZHs7k6H6xNY', editable=False, max_length=22),
        ),
    ]