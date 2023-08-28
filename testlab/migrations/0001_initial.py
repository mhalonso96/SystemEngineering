# Generated by Django 3.1.3 on 2023-08-28 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager', '0001_initial'),
        ('technician', '0001_initial'),
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestLab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ManyToManyField(to='department.Department')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.manager')),
                ('technician', models.ManyToManyField(to='technician.Technician')),
            ],
        ),
    ]
