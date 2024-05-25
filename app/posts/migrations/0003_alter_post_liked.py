# Generated by Django 5.0.6 on 2024-05-12 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_liked'),
        ('users', '0003_relationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(blank=True, related_name='liked', to='users.profile'),
        ),
    ]