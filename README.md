
Implementação de números por extenso. 

Requisitos para executar:
Python3
Django

git clone https://github.com/douglashiura/numero-por-extenso.git

cd numero-por-extenso		      -- Entrar no repositório    

python3 manage.py test		    -- Rodar os testes

python3 manage.py runserver	-- Rodar o serviço


Como usar:

Os números podem estar no intervalo [-999999, 999999].

Exemplos:

λ curl http://localhost:8000/1
{ "extenso": "um" }

λ curl http://localhost:8000/-1042
{ "extenso": "menos mil e quarenta e dois" }

λ curl http://localhost:8000/94587
{ "extenso": "noventa e quatro mil e quinhentos e oitenta e sete" }

OBS.: Certifique-se que o servidor está rodando na porta 8000 e o idioma pt-br é melhor para requisições.
