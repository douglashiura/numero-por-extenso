from django.utils.translation import ugettext as _


class Numero(object):
    
    def __init__(self, unidade="", preDezena="", dezena="", centena=""):
        self.unidade = _(unidade)
        self.preDezena = _(preDezena)
        self.dezena = _(dezena)
        self.centena = _(centena)
  
    def unidadePorExtenso(self):
        return self.unidade

    def preDezenaPorExtenso(self):
        return self.preDezena

    def dezenaPorExtenso(self):
        return self.dezena

    def centenaPorExtenso(self):
        return self.centena


        
class Seis(Numero):

    def __init__(self):
        super().__init__("seis", "dezesseis", "sessenta", "seiscentos")

        
class Sete(Numero):

    def __init__(self):
        super().__init__("sete", "dezessete", "setenta", "setecentos")
  
     
class Oito(Numero): 

    def __init__(self):
        super().__init__("oito"   , "dezoito", "oitenta", "oitocentos")   


class Nove(Numero):

    def __init__(self):
        super().__init__("nove", "dezenove", "noventa", "novecentos")
 
class Dois(Numero):

    def __init__(self):
        super().__init__("dois", "doze", "vinte", "duzentos")   

   
class Tres(Numero):

    def __init__(self):
        super().__init__("três"   , "treze"    , "trinta", "trezentos")   

 
class Quatro(Numero):

    def __init__(self):
        super().__init__("quatro", "quatorze", "quarenta", "quatrocentos")
 
    
class Cinco(Numero):

    def __init__(self):
        super().__init__("cinco"    , "quinze" , "cinquenta", "quinhentos")

class Zero(Numero):

    def __init__(self):
        super().__init__(unidade="zero", preDezena="dez", centena="")
    
    def dezenaPorExtenso(self):
        raise Exception
    
    def centenaPorExtenso(self):
        raise Exception

    
class Um(Numero):

    def __init__(self):
        super().__init__(unidade="um", preDezena="onze", centena="cento") 

    def dezenaPorExtenso(self):
        raise Exception

    def centenaPorExtenso(self, plural=True):
        return super().centenaPorExtenso() if plural else  _("cem")

     
