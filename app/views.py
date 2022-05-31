from django.contrib import messages
from django.shortcuts import render, redirect
from app.forms import noteForm
from app.models import About, Team, Feature


def index(request):
    _about = About.objects.all()
    _team = Team.objects.all()
    _feature = Feature.objects.all()

    context = {
        'lista': _about,
        'lista_team': _team,
        'lista_feature': _feature
    }
    return render(request, 'index.html', context)

def cadastrar_bloco(request):
    form = noteForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            messages.success(request, 'Registro realizado com sucesso')
            form.save()
            redirect('bloco/cadastrar')

        else:
            messages.error(request, 'Registro não pôde ser concluído')
    context = {
        'form': form
    }

    return render(request, 'bloco/cadastrar.html', context)


