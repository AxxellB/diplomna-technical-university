from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0002_auto_20201205_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='section',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('HOBBIES', 'Hobbies'), ('VIDEO', 'Video'), ('ARTS', 'Arts'), ('ENTERTAINMENT', 'Entertainment'), ('Q&As', 'Q&As'), ('PETS', 'Pets'), ('GAMING', 'Gaming'), ('SOCIAL', 'Social'), ('RANDOM', 'Random'), ('TECH', 'Tech'), ('SCIENCE', 'Science'), ('EDUCATION', 'Education'), ('POLITICS', 'Politics'), ('OTHER', 'Other')], default='Hobbies', max_length=15),
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
