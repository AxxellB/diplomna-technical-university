from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0017_auto_20201209_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_mature',
            field=models.CharField(choices=[('1', 'First'), ('2', 'Second')], max_length=128),
        ),
    ]
