# Generated by Django 5.0.6 on 2024-05-29 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("discordlogin", "0003_delete_film"),
    ]

    operations = [
        migrations.AddField(
            model_name="discorduser",
            name="avatar",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
