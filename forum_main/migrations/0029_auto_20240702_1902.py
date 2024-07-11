from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0028_auto_20240702_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rules',
            name='text',
            field=models.TextField(max_length=500),
        ),
    ]
