import requests

from acesso_cep import BuscaEndereco

cep = "01001000"

objeto_cep = BuscaEndereco(cep)
a = objeto_cep.acessa_via_cep()

print(a)
