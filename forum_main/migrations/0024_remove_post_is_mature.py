from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0023_auto_20201212_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_mature',
        ),
    ]
