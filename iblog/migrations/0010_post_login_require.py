# Generated by Django 3.2.15 on 2022-09-06 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iblog', '0009_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='login_require',
            field=models.BooleanField(default=False),
        ),
    ]
