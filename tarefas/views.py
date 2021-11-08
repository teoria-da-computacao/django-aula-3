from django.shortcuts import render


# Create your views here.
from tarefas.models import Tarefa

def index(request):
    return render(request, 'tarefas/index.html')

def listar(request):
    context = {'tarefas': Tarefa.objects.all()}
    return render(request, 'tarefas/lista.html', context)