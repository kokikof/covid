# Generated by Django 4.1.7 on 2023-03-09 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='FIO',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='test',
            name='resultat',
            field=models.CharField(max_length=15),
        ),
    ]
