# Generated by Django 4.1.5 on 2023-03-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_test_fio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='FIO',
            field=models.CharField(help_text='ваша фамилия', max_length=30, verbose_name='фио'),
        ),
        migrations.AlterField(
            model_name='test',
            name='data_sdachi',
            field=models.DateField(help_text='дата вашего теста', verbose_name='Дата сдачи'),
        ),
        migrations.AlterField(
            model_name='test',
            name='resultat',
            field=models.CharField(help_text='ваш результат на ковид', max_length=15, verbose_name='Результат'),
        ),
    ]
