# Generated by Django 2.1.7 on 2019-03-28 12:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('account_app', '0004_auto_20180504_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModifiedHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('order', models.BigIntegerField(db_index=True, null=True, verbose_name='히스토리 순서')),
                (
                'u_idx', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='u_idx')),
            ],
            options={
                'verbose_name': '사용자 정보 변경 내역',
                'verbose_name_plural': '사용자 정보 변경 내역 리스트',
                'db_table': 'user_modified_history',
            },
        ),
    ]
