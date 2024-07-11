from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0007_auto_20201207_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(choices=[('GAMING', 'Gaming'), ('NATURE', 'Nature'), ('ENTERTAINMENT', 'Entertainment'), ('SELFIE', 'Selfie'), ('CAMERA', 'Camera'), ('USERNAME', 'Username'), ('FUNNY', 'Funny'), ('PHOTOGRAPHY', 'Photography'), ('CLIMBING', 'Climbing'), ('ADVENTURE', 'Adventure'), ('DREAMS', 'Dreams'), ('LIFE', 'Life'), ('REASON', 'Reason'), ('SOCIAL', 'Social')], default='Social', max_length=15),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
