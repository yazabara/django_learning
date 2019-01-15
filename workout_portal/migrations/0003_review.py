from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_portal', '0002_img_vid_add'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=2000)),
                ('publication_date', models.DateTimeField()),
                ('entity_id', models.PositiveIntegerField()),
                ('entity_type', models.CharField(choices=[('SET', 'WorkoutSet'), ('EXC', 'Exercise'), ('TRN', 'Training'), ('VID', 'ExerciseVideo'), ('IMG', 'ExerciseImage')], max_length=3)),
            ],
        ),
    ]
