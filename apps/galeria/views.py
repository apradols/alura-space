from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.contrib import messages

def index(request):

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

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Efetue o login para ter acesso a galeria')
        return redirect('login')

    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova imagem cadastrada!')
            return redirect('index')

    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)
    
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem editada com sucesso!')
            return redirect('index')
        
    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})

def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, ' Imagem deletada com sucesso!')
    return redirect('index')