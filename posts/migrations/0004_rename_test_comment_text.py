# Generated by Django 4.0.5 on 2022-06-23 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='test',
            new_name='text',
        ),
    ]
