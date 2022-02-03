# Generated by Django 3.0.3 on 2021-11-26 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounting', '0004_startupcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='startup_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='useraccounting.StartupCategory'),
        ),
    ]
