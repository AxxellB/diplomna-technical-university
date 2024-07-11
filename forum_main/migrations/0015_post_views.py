from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0014_reply_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
