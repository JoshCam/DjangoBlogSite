# Generated by Django 3.1.7 on 2021-04-06 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='BlogPost',
        ),
    ]