from django.db import models
from django.utils import timezone

#Declaração das choices
SEXO_CHOICE = (
    ('M', 'MASCULINO'),
    ('F', 'FEMININO'),
)
ESTADO_CHOICE = (
    ('AC', 'ACRE'),
    ('AL', 'ALAGOAS'),
    ('AP', 'AMAPA'),
    ('AM', 'AMAZONAS'),
    ('BA', 'BAHIA'),
    ('CE', 'CEARA'),
    ('DF', 'DISTRITO FEDERAL'),
    ('ES', 'ESPIRITO SANTO'),
    ('GO', 'GOIAS'),
    ('MA', 'MARANHAO'),
    ('MT', 'MATO GROSSO'),
    ('MS', 'MATO GROSSO DO SUL'),
    ('MG', 'MINAS GERAIS'),
    ('PA', 'PARA'),
    ('PB', 'PARAIBA'),
    ('PR', 'PARANA'),
    ('PE', 'PERNAMBUCO'),
    ('PI', 'PIAUI'),
    ('RJ', 'RIO DE JANEIRO'),
    ('RN', 'RIO GRANDE DO NORTE'),
    ('RS', 'RIO GRANDE DO SUL'),
    ('RO', 'RONDONIA'),
    ('RR', 'RORAIMA'),
    ('SC', 'SANTA CATARINA'),
    ('SP', 'SAO PAULO'),
    ('SE', 'SERGIPE'),
    ('TO', 'TOCANTINS'),
)

#Definicao do model Pessoa
class Pessoa(models.Model):
	nome = models.CharField(
		max_length = 80
		)
	idade = models.IntegerField()
	sexo = models.CharField(
		max_length = 1, 
		choices = SEXO_CHOICE
		)
	endereco = models.CharField(
		max_length = 200
		)
	cep = models.IntegerField()
	bairro = models.CharField(
		max_length = 80
		)
	cidade = models.CharField(
		max_length = 80
		)
	estado = models.CharField(
		max_length = 2, 
		choices = ESTADO_CHOICE
		)
	cpf = models.IntegerField(
		max_length = 11
		)
	rg = models.IntegerField(
		max_length = 9
		)
	email = models.EmailField()
	dtn = models.DateField(
		'Data de nascimento', 
		default = timezone.now()
		)
	dts = models.DateTimeField(
		'Pessoa salva em', 
		blank = True, default = timezone.now()
		)

	def __str__(self):
		return self.nome