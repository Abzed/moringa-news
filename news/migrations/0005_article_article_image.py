# Generated by Django 3.1.2 on 2020-10-07 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='static/photos/user_square.jpg', upload_to='articles/'),
        ),
    ]
