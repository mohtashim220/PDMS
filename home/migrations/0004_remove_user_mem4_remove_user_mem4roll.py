# Generated by Django 5.0 on 2023-12-20 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_user_ledname_user_ledroll_user_mem1roll_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mem4',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mem4roll',
        ),
    ]
