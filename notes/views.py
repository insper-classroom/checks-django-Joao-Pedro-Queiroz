from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Olá mundo!</h1><p>Este é o app notes de <em>DevLife do Insper</em>.</p>")


def resposta_creditos(request):
     return HttpResponse("<h1>Créditos</h1><p>Sistema web desenvolvido por João Pedro Queiroz Viana</p>")