from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Livros.models import Livros_Id , Livros
from Livros.serializers import LivrosidSerializers, LivrosSerializers

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def livrosApi(request, id=0):
    if request.method=='GET':
        livros = Livros_Id.objects.all()
        livros_serializer= LivrosidSerializers(livros,many=True)
        return JsonResponse(livros_serializer.data,safe=False)
    elif request.method=='POST':
        livros_data=JSONParser().parse(request)
        livros_serializer = LivrosidSerializers(data = livros_data)
        if livros_serializer.is_valid():
            livros_serializer.save()
            return JsonResponse("Adicionado con sucesso", safe=False)
        return JsonResponse("Falha ao adicionar",safe=False)
    elif request.method=='PUT':
        livros_data=JSONParser().parse(request)
        livros=Livros_Id.objects.get(livros_id=livros_data['livros_id'])
        livros_serializer= LivrosidSerializers(livros,data=livros_data)
        if livros_serializer.is_valid():
            livros_serializer.save()
            return JsonResponse("Atualizado com sucesso",safe=False)
        return JsonResponse("Erro ao Atualizar")
    elif request.method=='DELETE':
        livros=Livros_Id.objects.get(livros_id=id)
        livros.delete()
        return JsonResponse('Deletado com sucesso',safe=False)

def livrosApid(request, id=0):
    if request.method=='GET':
        livros = Livros.objects.all()
        livros_serializer= LivrosSerializers(livros,many=True)
        return JsonResponse(livros_serializer.data,safe=False)
    elif request.method=='POST':
        livro_data=JSONParser().parse(request)
        livros_serializer = LivrosSerializers(data = livro_data)
        if livros_serializer.is_valid():
            livros_serializer.save()
            return JsonResponse("Adicionado con sucesso", safe=False)
        return JsonResponse("Falha ao adicionar",safe=False)
    elif request.method=='PUT':
        livro_data=JSONParser().parse(request)
        livro=Livros.objects.get(id=livro_data['id'])
        livros_serializer= LivrosSerializers(livro,data=livro_data)
        if livros_serializer.is_valid():
            livros_serializer.save()
            return JsonResponse("Atualizado com sucesso",safe=False)
        return JsonResponse("Erro ao Atualizar")
    elif request.method=='DELETE':
        livro=Livros.objects.get(id=id)
        livro.delete()
        return JsonResponse('Deletado com sucesso',safe=False)

@csrf_exempt
def SalvarArquivo(request):
    file=request.FILES['file']
    file_name = default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)

