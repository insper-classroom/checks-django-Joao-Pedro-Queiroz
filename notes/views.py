from django.http import HttpResponse
from django.shortcuts import render
from .models import Note

def index(request):
    all_notes = Note.objects.all().order_by("-created_at")

    return render(request, 'notes/index.html', {'notes': all_notes})

def resposta_creditos(request):
     return HttpResponse("<h1>Créditos</h1><p>Sistema web desenvolvido por João Pedro Queiroz Viana</p>")