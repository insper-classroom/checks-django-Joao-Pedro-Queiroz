from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Note

def index(request):
    if request.method == 'POST':
        nwe_note = Note(title=request.POST.get('titulo'), content=request.POST.get('detalhes'))
        nwe_note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all().order_by("-created_at")
        return render(request, 'notes/index.html', {'notes': all_notes})

def resposta_creditos(request):
     return HttpResponse("<h1>Créditos</h1><p>Sistema web desenvolvido por João Pedro Queiroz Viana</p>")