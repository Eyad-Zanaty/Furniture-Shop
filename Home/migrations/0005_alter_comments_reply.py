# Generated by Django 4.2.17 on 2025-02-10 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_alter_comments_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='reply',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Home.rebly'),
        ),
    ]
