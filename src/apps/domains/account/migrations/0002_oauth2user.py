# Generated by Django 2.0.2 on 2018-02-20 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuth2User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('name', models.CharField(max_length=16, unique=True, verbose_name='이름')),
            ],
            options={
                'verbose_name': 'oauth2 사용자 계정',
                'verbose_name_plural': 'oauth2 사용자 계정 리스트',
                'db_table': 'oauth2_user',
            },
        ),
    ]