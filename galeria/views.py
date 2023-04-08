from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.order_by("data").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografias = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografias})

def buscar(request):
    fotografias = Fotografia.objects.order_by("data").filter(publicada=True)
    if 'buscar' in request.GET:
        busca = request.GET['buscar']
        if busca:
            fotografias = fotografias.filter(nome__icontains=busca)

    return render(request, 'galeria/buscar.html', {'cards': fotografias})