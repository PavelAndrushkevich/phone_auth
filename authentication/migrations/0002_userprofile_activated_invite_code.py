# Generated by Django 4.2.4 on 2023-08-19 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='activated_invite_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
