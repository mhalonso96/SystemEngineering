# Generated by Django 3.1.3 on 2023-08-28 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testlab', '0002_auto_20230827_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='testlab',
            name='description',
            field=models.CharField(default=23, max_length=1000),
            preserve_default=False,
        ),
    ]