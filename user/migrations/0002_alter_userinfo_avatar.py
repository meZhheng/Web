# Generated by Django 4.0.3 on 2022-04-19 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.CharField(default='default.jpeg', max_length=100, verbose_name='头像'),
        ),
    ]
