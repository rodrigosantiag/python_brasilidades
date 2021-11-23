import re

from TelefonesBR import TelefonesBR

telefone = "551226481234"

telefone_objeto = TelefonesBR(telefone)
# padrao = "([0-9]{2,3})?([0-9]{2})?([0-9]{4,5})([0-9]{4})"
#
# resposta = re.findall(padrao, telefone)
# print(resposta)

print(telefone_objeto)
