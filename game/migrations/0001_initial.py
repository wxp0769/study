# Generated by Django 4.2.9 on 2025-01-14 19:56

from django.db import migrations, models
import game.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Game Name')),
                ('description', models.CharField(max_length=255, verbose_name='Game Description')),
                ('iframeTitle', models.CharField(max_length=50, verbose_name='Game Name')),
                ('iframeDescription', models.CharField(max_length=255, verbose_name='Game Description')),
                ('thumbnail', models.FileField(default='/avatars/default.png', upload_to=game.models.get_file_path)),
                ('iframePageUrl', models.CharField(max_length=50, verbose_name='Play_')),
                ('GamePageUrl', models.CharField(max_length=50, verbose_name='Game Name')),
                ('recommend', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create_time')),
                ('update_time', models.DateTimeField(auto_now_add=True, verbose_name='update_time')),
                ('content', models.TextField()),
                ('whatis', models.TextField()),
                ('HowtoPlay', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('site_url', models.CharField(max_length=32, verbose_name='站点域名')),
                ('site_name', models.CharField(max_length=64, verbose_name='站点名称')),
                ('logo', models.FileField(default='/avatars/default.png', upload_to=game.models.get_file_path)),
                ('title', models.CharField(max_length=64, verbose_name='SEO标题')),
                ('description', models.CharField(max_length=255, verbose_name='Game Description')),
            ],
        ),
    ]
