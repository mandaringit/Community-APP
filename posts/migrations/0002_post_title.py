# Generated by Django 2.2.6 on 2019-10-21 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='기본제목', max_length=150),
            preserve_default=False,
        ),
    ]
