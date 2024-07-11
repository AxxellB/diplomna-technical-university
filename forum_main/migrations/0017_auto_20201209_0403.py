from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0016_post_replies'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category_color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='tag_color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
