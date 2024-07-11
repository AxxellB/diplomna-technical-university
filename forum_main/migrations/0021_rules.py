from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_main', '0020_auto_20201209_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=20000)),
            ],
        ),
    ]
