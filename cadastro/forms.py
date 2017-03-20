from .models import Pessoa
from django.forms import ModelForm

class CadastroForm(ModelForm):
	class Meta:
		model = Pessoa
		exclude = ['',]