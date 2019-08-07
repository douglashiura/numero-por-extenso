import unittest
from extenso.numero.numeros import Numeros



class ExtensoTestCase(unittest.TestCase):

    def test_Extensos(self):
       
        self.assertEqual('zero', Numeros.extenso(0));
        self.assertEqual('um', Numeros.extenso(1));
        self.assertEqual('dois', Numeros.extenso(2));
        self.assertEqual('dez', Numeros.extenso(10));
        self.assertEqual('onze', Numeros.extenso(11));
        self.assertEqual('vinte', Numeros.extenso(20));
        self.assertEqual('vinte e um', Numeros.extenso(21));
        self.assertEqual('trinta', Numeros.extenso(30));
        self.assertEqual('cem', Numeros.extenso(100));
        self.assertEqual('cento e um', Numeros.extenso(101));
        self.assertEqual('cento e dois', Numeros.extenso(102));
        self.assertEqual('cento e dez', Numeros.extenso(110));
        self.assertEqual('cento e onze', Numeros.extenso(111));
        self.assertEqual('cento e vinte', Numeros.extenso(120));
        self.assertEqual('cento e vinte e um', Numeros.extenso(121));
        self.assertEqual('duzentos', Numeros.extenso(200));
        self.assertEqual('duzentos e dezessete', Numeros.extenso(217));
        self.assertEqual('mil', Numeros.extenso(1000));
        self.assertEqual('mil e um', Numeros.extenso(1001));
        self.assertEqual('mil e dez', Numeros.extenso(1010));
        self.assertEqual('mil e onze', Numeros.extenso(1011));
        self.assertEqual('mil e vinte', Numeros.extenso(1020));
        self.assertEqual('mil e cem', Numeros.extenso(1100));
        self.assertEqual('mil e cento e um', Numeros.extenso(1101));
        self.assertEqual('mil e cento e dez', Numeros.extenso(1110));
        self.assertEqual('mil e cento e onze', Numeros.extenso(1111));
        self.assertEqual('dois mil e cento e onze', Numeros.extenso(2111));
        self.assertEqual('nove mil e novecentos e noventa e nove', Numeros.extenso(9999));
        self.assertEqual('dez mil', Numeros.extenso(10000));
        self.assertEqual('onze mil', Numeros.extenso(11000));
        self.assertEqual('cem mil e um', Numeros.extenso(100001));
        self.assertEqual('cem mil e dez', Numeros.extenso(100010));
        self.assertEqual('cem mil e cem', Numeros.extenso(100100));
        self.assertEqual('cento e um mil', Numeros.extenso(101000));
        self.assertEqual('cento e um mil e um', Numeros.extenso(101001));
        self.assertEqual('cento e um mil e dez', Numeros.extenso(101010));
        self.assertEqual('cento e um mil e cem', Numeros.extenso(101100));
        self.assertEqual('cento e um mil e cento e um', Numeros.extenso(101101));
        self.assertEqual('cento e um mil e cento e dez', Numeros.extenso(101110));
        self.assertEqual('novecentos e noventa e nove mil e novecentos e noventa e nove', Numeros.extenso(999999));
        self.assertEqual('novecentos e noventa e nove mil e novecentos e noventa', Numeros.extenso(999990));
        self.assertEqual('novecentos e noventa e nove mil e novecentos', Numeros.extenso(999900));
        self.assertEqual('novecentos e noventa e nove mil', Numeros.extenso(999000));
        self.assertEqual('novecentos e noventa mil', Numeros.extenso(990000));
        self.assertEqual('novecentos mil', Numeros.extenso(900000));
        self.assertEqual('menos novecentos e noventa e nove', Numeros.extenso(-999));
        self.assertEqual('menos um', Numeros.extenso(-1));
        self.assertEqual('noventa e quatro mil e quinhentos e oitenta e sete', Numeros.extenso(94587));
        self.assertEqual('menos mil e quarenta e dois', Numeros.extenso(-1042));
        with self.assertRaises(Exception): Numeros.extenso("a")
        
