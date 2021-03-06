# Generated by Django 3.2.4 on 2021-12-13 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
                ('about', models.TextField(max_length=150)),
                ('icon_select', models.CharField(choices=[('lni-layers', 'ui_ux_design'), ('lni-tab', 'app_dev'), ('lni-cog', 'web_dev'), ('lni-briefcase', 'marketing'), ('lni-stats-up', 'grafico'), ('lni-pencil', 'caneta')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(max_length=80)),
                ('note', models.TextField(max_length=500)),
                ('notice', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'ordering': ['title', 'sub_title', 'note', 'notice', 'create_at', 'update_at'],
            },
        ),
    ]
