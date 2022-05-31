# Generated by Django 4.0.4 on 2022-05-30 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_about_icon_select_alter_feature_icon_select_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='icon_select',
            field=models.CharField(choices=[('lni-layers', 'ui_ux_design'), ('lni-cog', 'web_dev'), ('lni-tab', 'app_dev'), ('lni-pencil', 'caneta'), ('lni-stats-up', 'grafico'), ('lni-briefcase', 'marketing')], max_length=20),
        ),
        migrations.AlterField(
            model_name='feature',
            name='icon_select',
            field=models.CharField(choices=[('lni-rocket', 'foguete'), ('lni-database', 'dados'), ('lni-leaf', 'folha'), ('lni-tab', 'responsivo'), ('lni-pencil', 'caneta'), ('lni-layout', 'quadro')], max_length=20),
        ),
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
