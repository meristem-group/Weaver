# Generated by Django 4.0.4 on 2022-05-31 12:52

from django.db import migrations
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_glycerolstock_tablefilter_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restrictionenzyme',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='restrictionenzyme',
            name='cpg_methylation',
        ),
        migrations.RemoveField(
            model_name='restrictionenzyme',
            name='dam_methylation',
        ),
        migrations.RemoveField(
            model_name='restrictionenzyme',
            name='dcm_methylation',
        ),
        migrations.RemoveField(
            model_name='restrictionenzyme',
            name='fcut',
        ),
        migrations.RemoveField(
            model_name='restrictionenzyme',
            name='inactivation_temperature',
        ),
        migrations.RemoveField(
            model_name='restrictionenzyme',
            name='inactivation_time',
        ),
        migrations.RemoveField(
            model_name='restrictionenzyme',
            name='max_activity_temperature',
        ),
        migrations.RemoveField(
            model_name='restrictionenzyme',
            name='rcut',
        ),
        migrations.RemoveField(
            model_name='restrictionenzyme',
            name='recognition_site',
        ),
        migrations.RemoveField(
            model_name='restrictionenzyme',
            name='recommended_incubation_time',
        ),
        migrations.AlterField(
            model_name='glycerolstock',
            name='qr_id',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, default='fyEUwkfEdREZn8ZAtWPuda', editable=False, max_length=22),
        ),
        migrations.AlterField(
            model_name='plasmid',
            name='qr_id',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, default='mZoMpXCy3dRfjBndwRcdsD', editable=False, max_length=22),
        ),
        migrations.AlterField(
            model_name='primer',
            name='qr_id',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, default='JRhTueyDo4GgyWuFrypMSg', editable=False, max_length=22),
        ),
    ]