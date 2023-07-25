# Generated by Django 4.0.4 on 2022-07-22 15:02

from django.db import migrations, models
import django.db.models.deletion
import shortuuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0012_project_description'),
        ('inventory', '0020_delete_plasmidauthor_alter_glycerolstock_qr_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='glycerolstock',
            name='project',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='organization.project'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='glycerolstock',
            name='qr_id',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, default='JrhAKeYTzH9v7K2NWkWQvP', editable=False, max_length=22),
        ),
        migrations.AlterField(
            model_name='plasmid',
            name='qr_id',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, default='BgA6jUUYa5uDxeDb7xq87d', editable=False, max_length=22),
        ),
        migrations.AlterField(
            model_name='primer',
            name='qr_id',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, default='Yz8EhwfVJk5eBHGU5GhycR', editable=False, max_length=22),
        ),
    ]