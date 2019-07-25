
from django.urls import path

from django.urls.converters import register_converter
from extenso import views

class ConversorDeNumeros:
    regex = '(-)?[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return '%d' % value

register_converter(ConversorDeNumeros, 'number')

urlpatterns = [
     path("<number:numero>", views.numero_por_extenso, name="por-extenso"),
]


