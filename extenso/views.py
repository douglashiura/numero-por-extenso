from django.http.response import JsonResponse, HttpResponseNotFound
from django.utils.translation import ugettext as _
from extenso.numero.numeros import Numeros



def numero_por_extenso(request, numero):
    try:
        data = { "extenso": Numeros.extenso(numero) }     
        return JsonResponse(data)
    except:
        return HttpResponseNotFound(_("fora.do.intervalo"))

