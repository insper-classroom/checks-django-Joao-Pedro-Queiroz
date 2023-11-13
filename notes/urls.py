from django.urls import path
from . import views

urlpatterns = [
    path('creditos/', views.resposta_creditos),
    path('', views.index, name='index'),
]