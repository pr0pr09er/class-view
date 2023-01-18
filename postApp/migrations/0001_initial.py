# Generated by Django 4.1.2 on 2022-12-26 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('boss', models.CharField(max_length=30)),
                ('authors', models.ManyToManyField(to='postApp.author')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('date', models.DateField()),
                ('img', models.ImageField(upload_to='static/img')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postApp.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postApp.category')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postApp.publisher')),
            ],
        ),
    ]
