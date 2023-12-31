# Generated by Django 4.2.7 on 2023-11-19 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('caption', models.CharField(max_length=255, verbose_name='Legenda')),
                ('poster_url', models.URLField(max_length=300, null=True, verbose_name='URL do avião')),
                ('steps_url', models.URLField(max_length=300, null=True, verbose_name='URL das instruções')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='Comentário')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avioes.post')),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('posts', models.ManyToManyField(blank=True, to='avioes.post')),
            ],
        ),
    ]
