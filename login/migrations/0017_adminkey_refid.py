# Generated by Django 2.1.1 on 2018-10-13 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_adminkey'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminkey',
            name='refid',
            field=models.CharField(default='z', max_length=1),
        ),
    ]
