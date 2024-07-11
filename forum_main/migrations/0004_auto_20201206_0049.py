from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0003_auto_20201205_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('HOBBIES', 'Hobbies'), ('VIDEO', 'Video'), ('ARTS', 'Arts'), ('GAMING', 'Gaming'), ('EXCHANGE', 'Exchange'), ('ENTERTAINMENT', 'Entertainment'), ('SOCIAL', 'Social'), ('RANDOM', 'Random'), ('TECH', 'Tech'), ('SCIENCE', 'Science'), ('Q&As', 'Q&As'), ('PETS', 'Pets'), ('EDUCATION', 'Education'), ('POLITICS', 'Politics')], default='Hobbies', max_length=15),
        ),
    ]
