# Generated by Django 3.2.4 on 2023-11-22 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_teams_team_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='players.teams'),
        ),
    ]
