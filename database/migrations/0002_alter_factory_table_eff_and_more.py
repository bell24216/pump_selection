# Generated by Django 4.1.7 on 2023-03-30 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory_table',
            name='eff',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='factory_table',
            name='eff_status',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='factory_table',
            name='rpm',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='factory_table',
            name='se_quence',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='factory_table',
            name='tolerance',
            field=models.IntegerField(),
        ),
    ]