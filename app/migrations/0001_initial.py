# Generated by Django 3.1.2 on 2020-10-28 00:32

import ckeditor.fields
import ckeditor_uploader.fields
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
            name='Precipitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('conteudo', ckeditor.fields.RichTextField()),
                ('imagem', ckeditor_uploader.fields.RichTextUploadingField()),
                ('data', models.DateTimeField()),
                ('publicar', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tempertura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('conteudo', ckeditor.fields.RichTextField()),
                ('imagem', ckeditor_uploader.fields.RichTextUploadingField()),
                ('data', models.DateTimeField()),
                ('publicar', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('conteudo', ckeditor.fields.RichTextField()),
                ('imagem', ckeditor_uploader.fields.RichTextUploadingField()),
                ('data', models.DateTimeField()),
                ('publicar', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('url', models.CharField(max_length=100, unique=True)),
                ('fonte', models.CharField(max_length=100)),
                ('resumo', ckeditor.fields.RichTextField()),
                ('imagem', ckeditor_uploader.fields.RichTextUploadingField()),
                ('data', models.DateTimeField()),
                ('publicar', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]