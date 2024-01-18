# Generated by Django 4.2.7 on 2023-11-04 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='attributes',
        ),
        migrations.AddField(
            model_name='player',
            name='skill',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='speed',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='strength',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True),
        ),
        migrations.DeleteModel(
            name='Attributes',
        ),
    ]