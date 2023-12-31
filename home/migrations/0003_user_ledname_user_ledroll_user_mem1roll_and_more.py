# Generated by Django 5.0 on 2023-12-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ledname',
            field=models.CharField(default='username', editable=False, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='ledroll',
            field=models.CharField(default='000000', editable=False, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='mem1roll',
            field=models.CharField(default='000000', editable=False, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='mem2roll',
            field=models.CharField(default='000000', editable=False, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='mem3roll',
            field=models.CharField(default='000000', editable=False, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='mem4roll',
            field=models.CharField(default='000000', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='mem1',
            field=models.CharField(default='username', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='mem2',
            field=models.CharField(default='username', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='mem3',
            field=models.CharField(default='username', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='mem4',
            field=models.CharField(default='username', editable=False, max_length=50),
        ),
        migrations.AlterModelTable(
            name='user',
            table='GroupInfo',
        ),
    ]
