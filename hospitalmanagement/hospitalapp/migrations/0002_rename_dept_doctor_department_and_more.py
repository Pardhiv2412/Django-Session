# Generated by Django 4.2.5 on 2023-09-14 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='dept',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='ill',
            new_name='cause',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='email',
        ),
    ]
