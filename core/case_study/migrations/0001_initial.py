# Generated by Django 2.2.4 on 2019-09-05 13:00

import datetime
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
            name='CaseStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('date_submitted', models.DateTimeField(blank=True, null=True)),
                ('is_submitted', models.BooleanField(default=False)),
                ('is_anonymous', models.BooleanField(default=True)),
                ('date_last_edited', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('scr', models.FloatField(blank=True, null=True)),
                ('age_type', models.CharField(blank=True, choices=[('Y', 'Years'), ('M', 'Months')], default='Y', max_length=1)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('description', models.TextField(blank=True, null=True)),
                ('answer_a', models.TextField(blank=True, null=True)),
                ('answer_b', models.TextField(blank=True, null=True)),
                ('answer_c', models.TextField(blank=True, null=True)),
                ('answer_d', models.TextField(blank=True, null=True)),
                ('answer', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1, null=True)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('last_edited_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_edited_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TagRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case_study.CaseStudy')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case_study.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('case_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case_study.CaseStudy')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, null=True)),
                ('case_study', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case_study.CaseStudy')),
            ],
        ),
        migrations.AddField(
            model_name='casestudy',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='case_study.Question'),
        ),
    ]
