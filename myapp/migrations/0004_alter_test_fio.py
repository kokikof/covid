# Generated by Django 4.1.5 on 2023-03-18 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_test_fio_alter_test_data_sdachi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='FIO',
            field=models.CharField(help_text='ФАМИЛИЮ СКАЗАЛ', max_length=30, verbose_name='фио'),
        ),
    ]
