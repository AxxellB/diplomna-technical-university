from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0025_auto_20240702_1849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='replies',
            new_name='comments',
        ),
    ]
