# Generated by Django 4.1.3 on 2022-12-04 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_user_doc_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_number',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, unique=True),
        ),
    ]
