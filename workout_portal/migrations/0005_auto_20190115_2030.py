# Generated by Django 2.1.5 on 2019-01-15 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workout_portal', '0004_initial_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='training',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='workout_portal.Training'),
        ),
    ]
