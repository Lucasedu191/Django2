from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .forms import  ContatoForm, ProdutoModelForms
from .models import Produto




def index(request):
    context ={
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, "email enviado com sucesso")
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar o email')

    context = {
        'form' : form
    }
    return render(request, 'contato.html', context)

def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForms(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto salvo com sucesso')
                form = ProdutoModelForms()
            else:
                messages.error((request, 'Erro ao salvar produto.'))
        else:
            form = ProdutoModelForms()
        context = {
            'form': form
        }
        return render(request,'produto.html', context)
    else:
        return redirect('index')

