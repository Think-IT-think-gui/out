# Generated by Django 3.2.10 on 2022-10-05 22:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Handler', '0003_remove_user_info_image_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts_info',
            old_name='Type',
            new_name='User_Id',
        ),
        migrations.RemoveField(
            model_name='posts_info',
            name='User',
        ),
        migrations.AddField(
            model_name='user_info',
            name='Country',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_info',
            name='Email',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_info',
            name='Password',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
