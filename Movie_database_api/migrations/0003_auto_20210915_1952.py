# Generated by Django 3.2.6 on 2021-09-15 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Movie_database_api", "0002_alter_rating_movie"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rating",
            name="ip",
        ),
        migrations.AddField(
            model_name="rating",
            name="user_id",
            field=models.CharField(
                default=None, max_length=15, verbose_name="Id пользователя"
            ),
        ),
    ]
