# Generated by Django 5.1.2 on 2024-11-01 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0003_album_song'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('authors', models.ManyToManyField(related_name='book_author', to='web_app.author')),
            ],
        ),
    ]
