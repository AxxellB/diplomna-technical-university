from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0012_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='text',
            field=models.TextField(max_length=10000),
        ),
    ]
