# Generated by Django 2.2.1 on 2019-05-06 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NoticiasCrud', '0007_auto_20190506_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticiasmodelo',
            name='fecha',
            field=models.DateField(null=True),
        ),
    ]
