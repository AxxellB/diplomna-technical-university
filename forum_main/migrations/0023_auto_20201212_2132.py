from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0022_post_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rules',
            name='text',
            field=models.TextField(max_length=5000),
        ),
    ]
