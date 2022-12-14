# Generated by Django 4.1.2 on 2022-10-24 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("movie_app", "0005_alter_review_stars")]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="director",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="movies",
                to="movie_app.director",
            ),
        )
    ]
