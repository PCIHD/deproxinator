# Generated by Django 2.1.1 on 2018-10-09 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20181008_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='batch',
            field=models.CharField(default='None', max_length=256),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='division',
            field=models.CharField(default='None', max_length=256),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='lecture',
            field=models.CharField(default='None', max_length=256),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='lecturer',
            field=models.CharField(default='None', max_length=256),
        ),
    ]
