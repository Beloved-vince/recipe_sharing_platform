# Generated by Django 4.1.4 on 2023-04-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_recipe_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]
