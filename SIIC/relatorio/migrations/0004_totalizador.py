# Generated by Django 3.1.7 on 2021-05-18 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relatorio', '0003_total_produtos'),
    ]

    operations = [
        migrations.CreateModel(
            name='TOTALIZADOR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MOVIMENTO', models.CharField(max_length=50)),
                ('QUANTIDADE', models.PositiveIntegerField()),
                ('TOTAL', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'TOTALIZADOR',
                'managed': False,
            },
        ),
    ]
