# Generated by Django 4.2.7 on 2023-11-06 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_player_attributes_player_skill_player_speed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='position',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
