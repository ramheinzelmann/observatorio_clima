from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class Teams(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    cargo = models.CharField(max_length=100)
    funcao = models.CharField(max_length=100)
    realizacao = RichTextField()
    foto = RichTextUploadingField()
    lattes = models.CharField(max_length=100, unique=True)
    facebook = models.CharField(max_length=100, unique=True)
    instagram = models.CharField(max_length=100, unique=True)
    linkedin = models.CharField(max_length=100, unique=True)
    data = models.DateTimeField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Tempertura(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    conteudo = RichTextField()
    imagem = RichTextUploadingField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    data = models.DateTimeField()
    publicar = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Precipitacao(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    conteudo = RichTextField()
    imagem = RichTextUploadingField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    data = models.DateTimeField()
    publicar = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Queimadas(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    conteudo = RichTextField()
    imagem = RichTextUploadingField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    data = models.DateTimeField()
    publicar = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Alagamento(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    conteudo = RichTextField()
    imagem = RichTextUploadingField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    data = models.DateTimeField()
    publicar = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Reservatorios(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    conteudo = RichTextField()
    imagem = RichTextUploadingField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    data = models.DateTimeField()
    publicar = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Projetos(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    url = models.URLField(max_length=150)
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    resumo = RichTextField()
    imagem = RichTextUploadingField()
    data = models.DateTimeField()
    publicar = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Publicacoes(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    fonte = models.CharField(max_length=100)
    conteudo = RichTextField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    foto = RichTextUploadingField()
    data = models.DateTimeField()
    publicar = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Noticias(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    url = models.URLField(max_length=100)
    fonte = models.CharField(max_length=100, blank=True)
    resumo = RichTextField()
    imagem = RichTextUploadingField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    data = models.DateTimeField()
    publicar = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Pluviograma(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    imagem_mini_post = RichTextUploadingField()
    fonte = models.CharField(max_length=100, blank=True)
    data = models.DateTimeField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    publicar = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Dashboard(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    imagem_post = RichTextUploadingField()
    fonte = models.CharField(max_length=100, blank=True)
    data = models.DateTimeField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    publicar = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Imagens_Banner(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    imagem = RichTextUploadingField()
    data = models.DateTimeField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    publicar = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Post(models.Model):
    titulo = models.CharField(max_length=800, unique=True)
    texto = RichTextField()

    def __str__(self):
        return self.titulo