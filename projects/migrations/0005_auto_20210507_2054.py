# Generated by Django 3.2 on 2021-05-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20210507_2019'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': '项目表', 'verbose_name_plural': '项目表'},
        ),
        migrations.AlterField(
            model_name='projects',
            name='id',
            field=models.AutoField(help_text='id主键', primary_key=True, serialize=False, verbose_name='id主键'),
        ),
    ]
