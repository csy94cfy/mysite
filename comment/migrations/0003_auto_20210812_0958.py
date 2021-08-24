# Generated by Django 2.0 on 2021-08-12 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20210812_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='comment.Comment'),
        ),
    ]
