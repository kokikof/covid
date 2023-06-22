# Generated by Django 4.1.4 on 2023-05-29 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_test_fio_alter_test_io_alter_test_data_sdachi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='FIO',
            field=models.CharField(help_text='ваша фамилия', max_length=30, null=True, verbose_name='фио'),
        ),
        migrations.AlterField(
            model_name='test',
            name='IO',
            field=models.CharField(help_text='паспортные данные', max_length=30, null=True, verbose_name='номер и серия паспорта'),
        ),
        migrations.AlterField(
            model_name='test',
            name='data_sdachi',
            field=models.DateField(help_text='дата вашего теста', null=True, verbose_name='Дата сдачи'),
        ),
        migrations.AlterField(
            model_name='test',
            name='resultat',
            field=models.CharField(help_text='ваш результат на ковид', max_length=15, null=True, verbose_name='Результат'),
        ),
    ]
