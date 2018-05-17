# Generated by Django 2.0.2 on 2018-05-16 20:01

from django.db import migrations, models
import lib.django.db.mysql


class Migration(migrations.Migration):
    dependencies = [
        ('oauth2_app', '0003_auto_20180504_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='refreshtoken',
            name='revoked',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='is_in_house',
            field=lib.django.db.mysql.TinyBooleanField(default=False, verbose_name='내부 서비스 여부'),
        ),
        migrations.AlterField(
            model_name='refreshtoken',
            name='token',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterIndexTogether(
            name='refreshtoken',
            index_together={('token', 'revoked')},
        ),
    ]
