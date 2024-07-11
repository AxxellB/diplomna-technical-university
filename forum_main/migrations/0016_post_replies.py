from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0015_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='replies',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
