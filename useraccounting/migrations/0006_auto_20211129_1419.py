# Generated by Django 3.0.3 on 2021-11-29 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounting', '0005_startup_startup_group'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ideanestcheck',
            new_name='Ideanestchecking',
        ),
        migrations.RenameModel(
            old_name='Sessionideanest',
            new_name='Sessionideanesting',
        ),
        migrations.RenameModel(
            old_name='Submissionideanest',
            new_name='Submissionideanesting',
        ),
        migrations.RenameModel(
            old_name='Viewerideanest',
            new_name='Viewerideanesting',
        ),
    ]
