# Generated by Django 4.2.3 on 2023-08-01 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='readCount',
            field=models.IntegerField(default=0),
        ),
    ]
