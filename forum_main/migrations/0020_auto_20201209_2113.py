from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0019_auto_20201209_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_mature',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=128),
        ),
    ]
