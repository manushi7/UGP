# Generated by Django 4.1.3 on 2022-11-22 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='id_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user', unique=True),
        ),
    ]
