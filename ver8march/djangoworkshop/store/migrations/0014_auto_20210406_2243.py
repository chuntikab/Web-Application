# Generated by Django 3.1.5 on 2021-04-06 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20210406_2212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpoint',
            old_name='total_points',
            new_name='totalpoints',
        ),
    ]
