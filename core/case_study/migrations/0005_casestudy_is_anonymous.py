# Generated by Django 2.2.4 on 2019-08-28 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_study', '0004_auto_20190820_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudy',
            name='is_anonymous',
            field=models.BooleanField(default=True),
        ),
    ]
