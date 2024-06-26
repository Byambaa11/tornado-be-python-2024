# Generated by Django 5.0 on 2024-03-18 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_post', '0001_initial'),
        ('core_user', '0002_user_avatar_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='posts_liked',
            field=models.ManyToManyField(related_name='liked_by', to='core_post.post'),
        ),
    ]
