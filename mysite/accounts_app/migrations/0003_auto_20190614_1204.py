# Generated by Django 2.2.2 on 2019-06-14 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0002_auto_20190614_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programmer',
            old_name='Languages',
            new_name='languages',
        ),
    ]
