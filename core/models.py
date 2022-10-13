
from django.db import models
from stdimage.models import StdImageField



# Para evitar erros com imagens com mesmo nome pode por abaixo de a definição:

import uuid

def get_file_path(_instance, filename):
	ext = filename.split('.')[-1]
	filename = f'{uuid.uuid4()}.{ext}'
	return filename




# auto_now_add= True coloca data automaticamente
# auto_now=True  coloca data de atualização

class Base(models.Model):
    criados = models.DateField('Data de criação', auto_now_add= True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo: ', default=True)

    class Meta:
        abstract = True

# 1- icone:
# Pode criar tuplas e depois receber o conteúdo abaixo
class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráficos'),
        ('lni-users', 'Usuário'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.TextField('Ícone', max_length=13, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_plural = 'Serviços'

    def __str__(self):
        return self.servico



# 2- título(Cargo na empresa):

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_plural = 'Cargos'

    def __str__(self):
        return self.cargo



# 3- descrição(Funcionário):

# Vai criar um diretório equipe e por as imagens lá. 480 é o tamanho real da imagem e se precisar cortar --> Crop = pode recortar.
# Importante por "on_delete=models.CASCADE", se não houver mais o cargo o nome também será excluido.
# Em "thumbnail" é importante manter o nome do arquivo original. Ao final será dada instrução para criar uma Def para evitar erros de imagens com mesmo nome.

class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200 )
    imagem = StdImageField('Imagem', upload_to =  get_file_path,   variations={'thumb': {'width':480, 'height':480, 'crop': True}})

    facebook= models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_plural = 'Funcionários'

    def __str__(self):
        return self.nome


