# Generated by Django 3.2.15 on 2022-09-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20220901_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='updated_date',
            field=models.DateTimeField(null=True),
        ),
    ]