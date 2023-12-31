# Generated by Django 4.2.6 on 2023-10-14 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog_img_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pros')),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'blog_img_1',
            },
        ),
        migrations.CreateModel(
            name='blog_img_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pros')),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'blog_img_2',
            },
        ),
        migrations.CreateModel(
            name='blog_img_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pros')),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'blog_img_3',
            },
        ),
    ]
