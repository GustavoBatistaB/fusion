from django.contrib import admin

from .models import Cargo, Servicos, Funcionario, Sobre, Recursos, RecursosDireito


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servicos)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ('servico', 'descricao', 'icone', 'ativo', 'modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')


@admin.register(Sobre)
class SobreAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'sobre')


@admin.register(Recursos)
class RecursosAdmin(admin.ModelAdmin):
    list_display = ('recurso', 'descricao_recurso', 'icone_recurso', 'ativo', 'modificado')


@admin.register(RecursosDireito)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('recurso_direto', 'descricao_recurso_direito', 'icone_recurso_direito', 'ativo', 'modificado' )
