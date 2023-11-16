from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Note, Tag
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.method == 'POST':
        new_note = Note(title=request.POST.get('titulo'), content=request.POST.get('detalhes'), author=request.user)
        new_note.save()
        tags = request.POST.get('tag').split()

        for tag in tags:
            tag_confirm = Tag.objects.filter(tag=tag)
            if not tag_confirm:
                tag = Tag(tag=tag)
                tag.save()
            else:
                tag = tag_confirm[0]

            new_note.tags.add(tag)

        return redirect('index')
    else:
        user_notes = Note.objects.filter(author=request.user).order_by("-created_at")
        return render(request, 'notes/index.html', {'notes': user_notes})
    

def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('index')


@login_required
def edit_note(request, note_id): 
    if request.method == 'POST':
        note = Note.objects.get(id=note_id)
        note.title = request.POST.get('titulo')
        note.content = request.POST.get('detalhes')
        note.save()
        return redirect('index')
    else:
        note = Note.objects.get(id=note_id)
        return render(request, 'notes/edit.html', {'note': note})
    

@login_required
def tags(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    notes_tag = Note.objects.filter(tags=tag).order_by("-created_at")
    return render(request, 'notes/tags.html', {'notes_tag': notes_tag})


def resposta_creditos(request):
     return HttpResponse("<h1>Créditos</h1><p>Sistema web desenvolvido por João Pedro Queiroz Viana</p>")