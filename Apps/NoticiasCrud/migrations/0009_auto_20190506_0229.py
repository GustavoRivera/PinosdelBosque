# Generated by Django 2.2.1 on 2019-05-06 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NoticiasCrud', '0008_auto_20190506_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticiasmodelo',
            name='detalle',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='noticiasmodelo',
            name='fecha',
            field=models.CharField(default='14-2-1', max_length=8),
            preserve_default=False,
        ),
    ]
