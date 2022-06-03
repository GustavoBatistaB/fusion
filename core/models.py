import uuid
from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class Servicos(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'grafico'),
        ('lni-users', 'Usuarios'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Servico', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone',max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    linkedin = models.CharField('Linkedin', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Sobre(Base):
    titulo = models.CharField('titulo', max_length=200)
    sobre = models.CharField('sobre', max_length=300)

    class Meta:
        verbose_name = 'Sobre'

    def __str__(self):
        return self.sobre


class Recursos(Base):
    ICONE_RECURSOS = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'grafico'),
        ('lni-users', 'Usuarios'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Notebook'),
        ('lni-leaf', 'Folha'),
    )

    recurso = models.CharField('nome', max_length=100)
    descricao_recurso = models.CharField('descricao', max_length=200)
    icone_recurso = models.CharField('Icone', max_length=16, choices=ICONE_RECURSOS)

    def __str__(self):
        return self.recurso


class RecursosDireito(Base):
    ICONE_RECURSOS_DIREITO = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'grafico'),
        ('lni-users', 'Usuarios'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Notebook'),
        ('lni-leaf', 'Folha'),
    )
    recurso_direto = models.CharField('nome', max_length=100)
    descricao_recurso_direito = models.CharField('descricao', max_length=200)
    icone_recurso_direito = models.CharField('icone', max_length=200, choices=ICONE_RECURSOS_DIREITO)


def __str__(self):
    return self.recurso_direto
