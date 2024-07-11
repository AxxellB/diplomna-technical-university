from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0024_remove_post_is_mature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]
