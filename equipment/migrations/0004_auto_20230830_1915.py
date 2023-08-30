# Generated by Django 3.1.3 on 2023-08-30 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0003_auto_20230827_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='cabinet',
            field=models.PositiveIntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='equipment',
            name='shelf',
            field=models.PositiveIntegerField(default=12),
            preserve_default=False,
        ),
    ]
