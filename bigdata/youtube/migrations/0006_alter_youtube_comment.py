# Generated by Django 3.2.13 on 2023-03-30 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0005_alter_youtube_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtube',
            name='comment',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]