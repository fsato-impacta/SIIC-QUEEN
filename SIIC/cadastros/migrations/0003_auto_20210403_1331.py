# Generated by Django 3.1.7 on 2021-04-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_auto_20210403_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='quantidade_disponivel',
            field=models.PositiveIntegerField(verbose_name='Quantidade disponíve'),
        ),
    ]
