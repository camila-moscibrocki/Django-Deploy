# Generated by Django 3.0.3 on 2020-04-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Carros",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("modelo", models.CharField(max_length=30)),
                ("marca", models.CharField(max_length=30)),
                ("ano", models.DateField()),
            ],
        ),
    ]
