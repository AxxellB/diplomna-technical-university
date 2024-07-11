from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum_main', '0032_auto_20240703_0206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category_color',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tag_color',
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
