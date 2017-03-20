from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa
from .forms import CadastroForm

def home(request):
	data = {}
	data['saudacoes'] = 'Bem vindo ao cadastro de novas pessoas!'
	return render(request, 'cadastro_home.html', data)

def lista(request):
	texto = {}
	texto['lista_pessoas'] = Pessoa.objects.all()
	return render(request, 'cadastro_lista.html', texto)

def detalhe(request,pk):
	cadastro = Pessoa.objects.get(id=pk)
	return render(request, 'cadastro_detalhe.html', {'objeto':cadastro})

def atualizar(request,pk):
	cadastro = Pessoa.objects.get(id=pk)
	form = CadastroForm(request.POST or None, instance = cadastro)

	if form.is_valid():
		form.save()
		return redirect('cadastro_lista')
	return render(request, 'cadastro_atualizar.html', {'form':form})


def novo(request):
	form = CadastroForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('cadastro_home')
	return render(request, 'cadastro_novo.html', {'form':form})

def deletar(request,pk):
	cadastro = Pessoa.objects.get(id=pk)

	if request.method == 'POST':
		cadastro.delete()
		return redirect('cadastro_lista')
	return render(request, 'cadastro_deletar.html', {'objeto':cadastro})