# Generated by Django 4.1.3 on 2022-12-04 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_billing_id_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='doc_name',
            field=models.CharField(max_length=100),
        ),
    ]
