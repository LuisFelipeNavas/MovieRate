# Generated by Django 3.0.5 on 2020-05-01 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200430_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='movies',
            field=models.ManyToManyField(related_name='genres', to='app.Movie'),
        ),
    ]
