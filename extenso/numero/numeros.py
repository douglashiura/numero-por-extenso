from django.utils.translation import ugettext as _

from extenso.numero.intervalo import Unidade, PreDezena, Dezena, \
    Centena, Milhar, Intervalo


class Numeros(object):

    def extenso(numero):  # @NoSelf
        Asseguro(numero).ehInterio()
        extenso = Extensos.escrito(abs(numero))
        return _("menos ") + extenso if numero < 0 else extenso


class Extensos (object):
    INTERVALOS = [Unidade(), PreDezena(), Dezena(), Centena(), Milhar()]

    def escrito(numero):  # @NoSelf
        intervalo = Intervalo(range(0))
        for umIntervalo in Extensos.INTERVALOS:
            if umIntervalo.estaNoIntervalo(numero):
                intervalo = umIntervalo;  
        return intervalo.escrito(numero=numero) 

    
class Asseguro(object):

    def __init__(self, valor):
        self.valor = valor

    def ehInterio(self):
        try:
            int(self.valor)
        except ValueError:
            raise Exception
              
