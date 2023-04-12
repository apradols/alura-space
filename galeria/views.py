from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia
from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Efetue o login para ter acesso a galeria')
        return redirect('login')
    fotografias = Fotografia.objects.order_by("data").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografias = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografias})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Efetue o login para ter acesso a galeria')
        return redirect('login')
    fotografias = Fotografia.objects.order_by("data").filter(publicada=True)
    if 'buscar' in request.GET:
        busca = request.GET['buscar']
        if busca:
            fotografias = fotografias.filter(nome__icontains=busca)

    return render(request, 'galeria/buscar.html', {'cards': fotografias})