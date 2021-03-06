# Generated by Django 4.0.4 on 2022-05-30 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_about_icon_select'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('office', models.CharField(blank=True, max_length=50)),
                ('photo', models.ImageField(upload_to='img/')),
            ],
            options={
                'ordering': ['name', 'office', 'photo'],
            },
        ),
        migrations.AlterField(
            model_name='about',
            name='icon_select',
            field=models.CharField(choices=[('lni-tab', 'app_dev'), ('lni-layers', 'ui_ux_design'), ('lni-briefcase', 'marketing'), ('lni-cog', 'web_dev'), ('lni-stats-up', 'grafico'), ('lni-pencil', 'caneta')], max_length=20),
        ),
    ]
