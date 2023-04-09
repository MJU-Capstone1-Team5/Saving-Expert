# Generated by Django 4.1.7 on 2023-04-09 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Myuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=50, null=True, verbose_name='이름')),
                ('password', models.CharField(max_length=50, null=True, verbose_name='비밀번호')),
                ('nickname', models.CharField(max_length=50, null=True, verbose_name='비밀번호')),
                ('email', models.CharField(max_length=50, null=True, verbose_name='비밀번호')),
                ('userimage', models.ImageField(blank=True, null=True, upload_to='userimage/', verbose_name='유저사진')),
                ('usermemo', models.TextField(verbose_name='유저소개')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
