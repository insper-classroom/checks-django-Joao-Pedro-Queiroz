from django.urls import path
from . import views

urlpatterns = [
    path('creditos/', views.resposta_creditos),
    path('anotacoes/<int:note_id>/apagar', views.delete_note, name='delete_note'),
    path('anotacoes/<int:note_id>', views.edit_note, name='edit_note'),
    path('', views.index, name='index'),
]