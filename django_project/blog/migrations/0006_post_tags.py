# Generated by Django 2.2.6 on 2019-10-07 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191007_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(default='tags', max_length=100),
        ),
    ]
