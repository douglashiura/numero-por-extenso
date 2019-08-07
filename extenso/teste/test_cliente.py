
import unittest

from django.test import Client

class ClienteTestCase(unittest.TestCase):

    def setUp(self):
        self.cliente = Client()

    def testPorExtensoZero(self):
        resposta=self.cliente.get("/0")
        self.assertEqual('zero',resposta.json()['extenso']);
        self.assertEqual(200,resposta.status_code);

    def testPorExtensoMenos1(self):
        resposta=self.cliente.get("/-1")
        self.assertEqual('menos um',resposta.json()['extenso']);
        self.assertEqual(200,resposta.status_code);
    
    def testPorExtenso1(self):
        resposta=self.cliente.get("/1")
        self.assertEqual('um',resposta.json()['extenso']);
        self.assertEqual(200,resposta.status_code);
    
    def testPorExtensoMenos999999(self):
        resposta=self.cliente.get("/-999999")
        self.assertEqual('menos novecentos e noventa e nove mil e novecentos e noventa e nove',resposta.json()['extenso']);
        self.assertEqual(200,resposta.status_code);
    
    def testPorExtenso1000000(self):
        resposta=self.cliente.get("/1000000")
        self.assertEqual(b'fora.do.intervalo',resposta.content);
        self.assertEqual(404,resposta.status_code);
    
    def testPorExtensoAbc(self):
        resposta=self.cliente.get("/abc")
        self.assertEqual(404,resposta.status_code);
    