from django.db import models

# Create your models here.

class Livros_Id(models.Model):
    livros_id = models.AutoField(primary_key=True)
    livroNome = models.CharField(max_length=30)
 

class Livros(models.Model):
    id = models.AutoField(primary_key=True)
    cod_livro = models.CharField(max_length=30)
    ISBN = models.CharField(max_length=30)
    Titulo_livro = models.CharField(max_length=30)
    autor_livro = models.CharField(max_length=30)
    edicao_livro = models.CharField(max_length=30)
    ano_ancamento = models.CharField(max_length=30)
    cod_biblioteca = models.IntegerField()
    link_livro = models.CharField(max_length=30)
    status_livro = models.CharField(max_length=30)

