from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0027_auto_20240702_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='text',
            field=models.TextField(max_length=1000),
        ),
    ]
