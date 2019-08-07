import abc

from django.utils.translation import ugettext as _

from extenso.numero.numero import Zero, Um, Dois, Tres, Quatro, Cinco, Seis, \
    Sete, Oito, Nove


class Intervalo(object):
    NUMEROS = [Zero(), Um(), Dois(), Tres(), Quatro(), Cinco(), Seis(), Sete(), Oito(), Nove()]

    def __init__(self, intervalo):
        self.intervalo = intervalo
        
    def estaNoIntervalo(self, numero):
        return numero in self.intervalo    

    @abc.abstractmethod
    def escrito(self):
        raise Exception 


class Milhar(Intervalo):

    def __init__(self):
        super().__init__(range(1000, 1000000))
  
    def milhar(self):
        return _("mil")

    def escrito(self, numero):
        from extenso.numero.numeros import Extensos  
        centena = numero % 1000;
        centena = _("") if  centena == 0 else _(" e ") + Extensos.escrito(centena)  
        milhares = int(numero / 1000)
        milhares = Extensos.escrito(milhares) + _(" ") if milhares > 1 else _("") 
        return milhares + self.milhar() + centena;  

    
class Centena(Intervalo):

    def __init__(self):
        super().__init__(range(100, 1000))
        
    def escrito(self, numero):
        if numero == 100:
            return Intervalo.NUMEROS[1].centenaPorExtenso(plural=False)
        dezena = numero % 100;
        from extenso.numero.numeros import Extensos
        dezena = _("") if  dezena == 0 else _(" e ") + Extensos.escrito(dezena) 
        return Intervalo.NUMEROS[int(numero / 100)].centenaPorExtenso() + dezena;  


class Dezena(Intervalo):

    def __init__(self):
        super().__init__(range(20, 100))

    def escrito(self, numero): 
        from extenso.numero.numeros import Extensos
        unidade = numero % 10;
        unidade = _("") if  unidade == 0 else _(" e ") + Extensos.escrito(unidade)  
        return Intervalo.NUMEROS[int(numero / 10)].dezenaPorExtenso() + unidade;  


class Unidade(Intervalo):

    def __init__(self):
        super().__init__(range(0, 10))

    def escrito(self, numero):
        return Intervalo.NUMEROS[numero].unidadePorExtenso()


class PreDezena(Intervalo):

    def __init__(self):
        super().__init__(range(10, 20))

    def escrito(self, numero):
        return Intervalo.NUMEROS[numero % 10].preDezenaPorExtenso()

