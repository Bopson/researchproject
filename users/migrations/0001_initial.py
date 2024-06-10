# Generated by Django 4.2.7 on 2023-11-04 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=15)),
                ('last', models.CharField(max_length=20)),
                ('attributes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='users.attributes')),
            ],
        ),
    ]
