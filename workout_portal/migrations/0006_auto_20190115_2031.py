# Generated by Django 2.1.5 on 2019-01-15 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workout_portal', '0005_auto_20190115_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutset',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to='workout_portal.Exercise'),
        ),
    ]
