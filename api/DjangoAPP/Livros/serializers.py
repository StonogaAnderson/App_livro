from django.db.models import fields
from rest_framework import serializers
from Livros.models import  Livros_Id, Livros

class LivrosidSerializers(serializers.ModelSerializer):
    class Meta:
        model = Livros_Id
        fields=('livros_id','livroNome')


class LivrosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Livros
        fields=('id','cod_livro','ISBN','Titulo_livro','autor_livro','edicao_livro','ano_ancamento','cod_biblioteca','link_livro','status_livro')

