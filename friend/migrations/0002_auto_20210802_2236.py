# Generated by Django 3.2.6 on 2021-08-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='facebook_handle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='friend',
            name='github_handle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='friend',
            name='instagram_handle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='friend',
            name='twitter_handle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='friend',
            name='youtube_handle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
