# Generated by Django 4.1.4 on 2023-05-01 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_username_rating_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='fullname',
        ),
        migrations.AddField(
            model_name='comment',
            name='fullname',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
