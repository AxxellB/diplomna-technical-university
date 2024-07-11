from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum_auth', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
