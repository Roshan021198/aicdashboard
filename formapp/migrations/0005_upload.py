# Generated by Django 3.0.3 on 2021-03-10 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0004_auto_20210309_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='pitchfile')),
            ],
        ),
    ]
