from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0018_auto_20201209_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_mature',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], max_length=128),
        ),
    ]
