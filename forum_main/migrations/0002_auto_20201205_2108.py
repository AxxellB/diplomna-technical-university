from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Thread',
            new_name='Post',
        ),
        migrations.AlterField(
            model_name='section',
            name='category',
            field=models.CharField(choices=[('HOBBIES', 'Hobbies'), ('VIDEO', 'Video'), ('ARTS', 'Arts'), ('ENTERTAINMENT', 'Entertainment'), ('Q&As', 'Q&As'), ('PETS', 'Pets'), ('GAMING', 'Gaming'), ('SOCIAL', 'Social'), ('RANDOM', 'Random'), ('TECH', 'Tech'), ('SCIENCE', 'Science'), ('EDUCATION', 'Education'), ('POLITICS', 'Politics'), ('OTHER', 'Other')], default='Hobbies', max_length=15),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
