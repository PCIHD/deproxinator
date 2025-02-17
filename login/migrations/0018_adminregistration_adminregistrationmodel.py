# Generated by Django 2.1.1 on 2018-10-22 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0017_adminkey_refid'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic1', models.ImageField(blank=True, upload_to='login/media/admin')),
                ('lecture', models.CharField(default='None', max_length=256)),
                ('lecturer', models.CharField(default='None', max_length=256)),
                ('id_no', models.CharField(default='0', max_length=20)),
                ('phone', models.CharField(default='0', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdminRegistrationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default='0', max_length=10)),
                ('id_no', models.CharField(default='null', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
