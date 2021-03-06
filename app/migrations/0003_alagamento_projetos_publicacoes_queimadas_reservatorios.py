# Generated by Django 3.1.2 on 2020-10-30 00:14

import ckeditor.fields
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20201029_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservatorios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('conteudo', ckeditor.fields.RichTextField()),
                ('imagem', ckeditor_uploader.fields.RichTextUploadingField()),
                ('data', models.DateTimeField()),
                ('publicar', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Queimadas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('conteudo', ckeditor.fields.RichTextField()),
                ('imagem', ckeditor_uploader.fields.RichTextUploadingField()),
                ('data', models.DateTimeField()),
                ('publicar', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('conteudo', ckeditor.fields.RichTextField()),
                ('foto', ckeditor_uploader.fields.RichTextUploadingField()),
                ('data', models.DateTimeField()),
                ('publicar', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Projetos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('url', models.CharField(max_length=100, unique=True)),
                ('resumo', ckeditor.fields.RichTextField()),
                ('imagem', ckeditor_uploader.fields.RichTextUploadingField()),
                ('data', models.DateTimeField()),
                ('publicar', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Alagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True)),
                ('conteudo', ckeditor.fields.RichTextField()),
                ('imagem', ckeditor_uploader.fields.RichTextUploadingField()),
                ('data', models.DateTimeField()),
                ('publicar', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
