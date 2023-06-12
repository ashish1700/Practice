# Generated by Django 4.0 on 2023-04-13 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('superadmin', 'Super Admin'), ('admin', 'Admin'), ('student', 'Student')], default='exit', max_length=20),
            preserve_default=False,
        ),
    ]