# Generated by Django 2.2.1 on 2019-05-02 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NoticiasCrud', '0002_remove_noticiasmodelo_cupos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticiasmodelo',
            name='Familia',
        ),
    ]
