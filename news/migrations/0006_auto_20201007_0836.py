# Generated by Django 3.1.2 on 2020-10-07 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_article_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='media/articles/user_square.jpg', upload_to='articles/'),
        ),
    ]
