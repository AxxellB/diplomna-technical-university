from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0026_auto_20240702_1855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='comments',
            new_name='replies',
        ),
    ]
