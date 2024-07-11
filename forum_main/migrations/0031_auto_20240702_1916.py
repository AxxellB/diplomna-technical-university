from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum_main', '0030_rules_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rules',
            new_name='Rule',
        ),
    ]
