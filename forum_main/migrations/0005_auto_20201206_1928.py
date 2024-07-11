from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0004_auto_20201206_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_mature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(choices=[('GAMING', 'Gaming'), ('NATURE', 'Nature'), ('ENTERTAINMENT', 'Entertainment'), ('SELFIE', 'Selfie'), ('CAMERA', 'Camera'), ('USERNAME', 'Username'), ('FUNNY', 'Funny'), ('PHOTOGRAPHY', 'Photography'), ('CLIMBING', 'Climbing'), ('ADVENTURE', 'Adventure'), ('DREAMS', 'Dreams'), ('LIFE', 'Life'), ('REASON', 'Reason'), ('SOCIAL', 'Social')], default='Social', max_length=15),
        ),
    ]
