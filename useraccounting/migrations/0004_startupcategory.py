# Generated by Django 3.0.3 on 2021-11-26 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounting', '0003_auto_20210511_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='StartupCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startupHub', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
