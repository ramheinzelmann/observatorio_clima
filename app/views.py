
from django.shortcuts import render

from app.app import noticias_home, pluviograma_home, dashboard_home
from app.sql import get_noticias, get_pluviograma, get_dashboard
from app.models import Noticias, Tempertura, Precipitacao, Teams, Publicacoes, Imagens_Banner, Queimadas, \
    Alagamento, Reservatorios, Post, Projetos


def index(request):

    retorno_pluviograma = get_pluviograma()
    pluviogramas = pluviograma_home(retorno_pluviograma)

    retorno_dashboard = get_dashboard()
    dashboards = dashboard_home(retorno_dashboard)

    noticias = get_noticias()
    noticia01, noticia02 = noticias_home(noticias)

    teams = Teams.objects.all()
    banner = Imagens_Banner.objects.all()

    posts = Post.objects.all()
    for i in posts:
        post = i

    return render(request, 'index.html', {'noticia01': noticia01, 'noticia02': noticia02, 'teams': teams,
                                          'dashboards': dashboards, 'pluviogramas': pluviogramas,
                                          'banner': banner, 'post': post})


def noticias(request):

    noticias = Noticias.objects.all()
    if not noticias:
        return render(request, 'app/noticias.html')

    return render(request, 'app/noticias.html', {'dados': noticias})


def temperatura(request):

    temperatura = Tempertura.objects.all()
    if not temperatura:
        return render(request, 'app/temperatura.html')

    return render(request, 'app/temperatura.html', {'dados': temperatura})


def precipitacao(request):

    precipitacao = Precipitacao.objects.all()
    if not precipitacao:
        return render(request, 'app/precipitacao.html')

    return render(request, 'app/precipitacao.html', {'dados': precipitacao})


def publicacoes(request):

    publicacoes = Publicacoes.objects.all()
    if not publicacoes:
        return render(request, 'app/publicacoes.html')

    return render(request, 'app/publicacoes.html', {'dados': publicacoes})


def queimada(request):

    queimada = Queimadas.objects.all()
    if not queimada:
        return render(request, 'app/queimada.html')

    return render(request, 'app/queimada.html', {'dados': queimada})


def alagamento(request):

    alagamento = Alagamento.objects.all()
    if not alagamento:
        return render(request, 'app/alagamento.html')

    return render(request, 'app/alagamento.html', {'dados': alagamento})


def reservatorio(request):

    reservatorio = Reservatorios.objects.all()
    if not reservatorio:
        return render(request, 'app/reservatorio.html')

    return render(request, 'app/reservatorio.html', {'dados': reservatorio})


def projetos(request):

    projetos = Projetos.objects.all()
    if not projetos:
        return render(request, 'app/projetos.html')

    return render(request, 'app/projetos.html', {'dados': projetos})


def glossario(request):

    # glossario = Glossario.objects.all()
    if not glossario:
        return render(request, 'app/glossario.html')

    return render(request, 'app/glossario.html', {'dados': glossario})


def lcgea(request):

    publicacoes = Publicacoes.objects.all()

    for texto in publicacoes:
        conteudo = texto
        print(conteudo)

    if not publicacoes:
        return render(request, 'app/sobre_lcgea.html')

    return render(request, 'app/sobre_lcgea.html', {'dados': publicacoes})
