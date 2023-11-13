from django.http import HttpResponse
from .models import Note

def index(request):
    conteudo = '<h1>Get-it</h1>'
    all_notes = Note.objects.all().order_by("-created_at")

    for id, note in enumerate(all_notes):
        if id == 0:
            conteudo += f'<ul><li>{note.title}</li>'
        elif id == len(all_notes) - 1:
            conteudo += f'<li>{note.title}</li></ul>'
        else:
            conteudo += f'<li>{note.title}</li>'

    return HttpResponse(conteudo)


def resposta_creditos(request):
     return HttpResponse("<h1>Créditos</h1><p>Sistema web desenvolvido por João Pedro Queiroz Viana</p>")