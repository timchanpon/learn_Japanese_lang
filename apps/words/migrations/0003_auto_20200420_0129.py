# Generated by Django 3.0.5 on 2020-04-19 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='romaji',
            field=models.CharField(default='a', max_length=3),
            preserve_default=False,
        ),
    ]