# Generated by Django 4.1.7 on 2023-04-17 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='date',
            field=models.TextField(blank=True, default='null', null=True, verbose_name='저장날짜'),
        ),
    ]