# Generated by Django 4.1.4 on 2023-04-03 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_test_io'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='data_sdachi',
            field=models.DateField(help_text='дата вашего теста', null=True, verbose_name='Дата сдачи'),
        ),
    ]
