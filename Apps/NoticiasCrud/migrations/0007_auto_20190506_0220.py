# Generated by Django 2.2.1 on 2019-05-06 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NoticiasCrud', '0006_noticiasmodelo_detalle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticiasmodelo',
            name='fecha',
            field=models.DateField(),
        ),
    ]
