# Generated by Django 3.0.4 on 2020-09-06 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_url_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='url_name',
            field=models.CharField(default='ok', editable=False, max_length=80, verbose_name='url name'),
        ),
    ]
