# Generated by Django 3.0.4 on 2020-08-29 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200829_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='ok-boomer-for-now', editable=False, max_length=120),
            preserve_default=False,
        ),
    ]