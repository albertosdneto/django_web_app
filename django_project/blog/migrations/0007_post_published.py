# Generated by Django 2.2.6 on 2019-10-07 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]