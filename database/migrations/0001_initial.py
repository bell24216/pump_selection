# Generated by Django 4.1.7 on 2023-03-30 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='factory_table',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('fac_number', models.CharField(max_length=20, null=True)),
                ('equipment', models.CharField(max_length=50, null=True)),
                ('brand', models.CharField(max_length=50, null=True)),
                ('model_short', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=50, null=True)),
                ('data_type', models.CharField(max_length=10, null=True)),
                ('se_quence', models.IntegerField(max_length=11)),
                ('rpm', models.IntegerField(max_length=11, null=True)),
                ('imp_dia', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('flow', models.DecimalField(decimal_places=4, max_digits=15, null=True)),
                ('head', models.DecimalField(decimal_places=4, max_digits=15, null=True)),
                ('eff', models.IntegerField(max_length=11, null=True)),
                ('npshr', models.DecimalField(decimal_places=4, max_digits=15, null=True)),
                ('kw', models.DecimalField(decimal_places=4, max_digits=15, null=True)),
                ('curve_format', models.CharField(max_length=20)),
                ('eff_rl', models.CharField(max_length=10)),
                ('eff_status', models.IntegerField(max_length=1)),
                ('eff_distance', models.DecimalField(decimal_places=4, max_digits=15)),
                ('tolerance', models.IntegerField(max_length=11)),
                ('scale_xy', models.DecimalField(decimal_places=4, max_digits=15)),
            ],
        ),
    ]
