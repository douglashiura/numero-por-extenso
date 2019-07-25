from django.test import TestCase

from extenso.numero.numero import Zero, Um, Dois, Tres, Quatro, \
    Cinco, Seis, Sete, Oito, Nove


class NumeroTestCase(TestCase):
    
    def test_zero(self):
        numero = Zero()
        self.assertEqual('zero', numero.unidadePorExtenso())
        self.assertEqual('dez', numero.preDezenaPorExtenso())
        with self.assertRaises(Exception): numero.dezenaPorExtenso()
        with self.assertRaises(Exception): numero.centenaPorExtenso()
    
    def test_um(self):
        numero = Um()
        self.assertEqual('um', numero.unidadePorExtenso())
        self.assertEqual('onze', numero.preDezenaPorExtenso())
        with self.assertRaises(Exception): numero.dezenaPorExtenso()
        self.assertEqual('cem', numero.centenaPorExtenso(plural=False))
        self.assertEqual('cento', numero.centenaPorExtenso())
        
    def test_dois(self):
        numero = Dois()
        self.assertEqual('dois', numero.unidadePorExtenso())
        self.assertEqual('doze', numero.preDezenaPorExtenso())
        self.assertEqual('vinte', numero.dezenaPorExtenso())
        self.assertEqual('duzentos', numero.centenaPorExtenso())

    def test_tres(self):
        numero = Tres()
        self.assertEqual('três', numero.unidadePorExtenso())
        self.assertEqual('treze', numero.preDezenaPorExtenso())
        self.assertEqual('trinta', numero.dezenaPorExtenso())
        self.assertEqual('trezentos', numero.centenaPorExtenso())
        
    def test_quatro(self):
        numero = Quatro()
        self.assertEqual('quatro', numero.unidadePorExtenso())
        self.assertEqual('quatorze', numero.preDezenaPorExtenso())
        self.assertEqual('quarenta', numero.dezenaPorExtenso())
        self.assertEqual('quatrocentos', numero.centenaPorExtenso())
    
    def test_cinco(self):
        numero = Cinco()
        self.assertEqual('cinco', numero.unidadePorExtenso())
        self.assertEqual('quinze', numero.preDezenaPorExtenso())
        self.assertEqual('cinquenta', numero.dezenaPorExtenso())
        self.assertEqual('quinhentos', numero.centenaPorExtenso())

    def test_seis(self):
        numero = Seis()
        self.assertEqual('seis', numero.unidadePorExtenso())
        self.assertEqual('dezesseis', numero.preDezenaPorExtenso())
        self.assertEqual('sessenta', numero.dezenaPorExtenso())
        self.assertEqual('seiscentos', numero.centenaPorExtenso())

    def test_sete(self):
        numero = Sete()
        self.assertEqual('sete', numero.unidadePorExtenso())
        self.assertEqual('dezessete', numero.preDezenaPorExtenso())
        self.assertEqual('setenta', numero.dezenaPorExtenso())
        self.assertEqual('setecentos', numero.centenaPorExtenso())

    def test_oito(self):
        numero = Oito()
        self.assertEqual('oito', numero.unidadePorExtenso())
        self.assertEqual('dezoito', numero.preDezenaPorExtenso())
        self.assertEqual('oitenta', numero.dezenaPorExtenso())
        self.assertEqual('oitocentos', numero.centenaPorExtenso())
 
    def test_nove(self):
        numero = Nove()
        self.assertEqual('nove', numero.unidadePorExtenso())
        self.assertEqual('dezenove', numero.preDezenaPorExtenso())
        self.assertEqual('noventa', numero.dezenaPorExtenso())
        self.assertEqual('novecentos', numero.centenaPorExtenso())
    
