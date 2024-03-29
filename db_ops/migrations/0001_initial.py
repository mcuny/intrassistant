# Generated by Django 2.1 on 2019-09-10 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.CharField(db_index=True, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('documentation', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='HardwareCable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('name', models.CharField(db_index=True, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(max_length=255)),
                ('subLocation', models.OneToOneField(null=True, on_delete='', to='db_ops.Location')),
            ],
        ),
        migrations.CreateModel(
            name='NetworkCable',
            fields=[
                ('id', models.CharField(db_index=True, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('location', models.OneToOneField(null=True, on_delete='', to='db_ops.Location')),
            ],
        ),
        migrations.CreateModel(
            name='PowerCable',
            fields=[
                ('id', models.CharField(db_index=True, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('location', models.OneToOneField(null=True, on_delete='', to='db_ops.Location')),
            ],
        ),
        migrations.AddField(
            model_name='hardwarecable',
            name='cable',
            field=models.OneToOneField(null=True, on_delete='', to='db_ops.NetworkCable'),
        ),
        migrations.AddField(
            model_name='hardwarecable',
            name='hardware',
            field=models.OneToOneField(null=True, on_delete='', to='db_ops.Hardware'),
        ),
        migrations.AddField(
            model_name='hardware',
            name='location',
            field=models.OneToOneField(null=True, on_delete='', to='db_ops.Location'),
        ),
        migrations.AddField(
            model_name='hardware',
            name='power',
            field=models.OneToOneField(null=True, on_delete='', to='db_ops.PowerCable'),
        ),
    ]
