# Generated by Django 3.1.7 on 2021-04-25 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('name', '0009_auto_20210425_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]
