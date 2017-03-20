from django.contrib import admin
from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
	list_display = ('nome', 'idade', 'sexo', 'endereco', 'cep', 'bairro', 'cidade', 'estado', 'cpf', 'rg', 'email', 'dtn', 'dts',)
	search_fields = ('nome', 'idade', 'sexo','cep', 'bairro', 'cidade', 'estado', 'cpf', 'rg', 'dtn', 'dts',)
	ordering = ('nome',)
	date_hierarchy = ('dtn')
	readondly_fields = ('dts',)

admin.site.register(Pessoa, PessoaAdmin)