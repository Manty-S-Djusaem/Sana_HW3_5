# Generated by Django 4.1.2 on 2022-10-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("movie_app", "0006_alter_movie_director")]

    operations = [
        migrations.AlterField(
            model_name="movie", name="duration", field=models.IntegerField(null=True)
        )
    ]
