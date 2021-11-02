from cpf_cnpj import Documento
from validate_docbr import CNPJ

exemplo_cnpj = "26044340000108"
exemplo_cpf = "76567524049"
exemplo_cpf_invalido = "11111111112"
# cnpj = CNPJ()
# print(cnpj.validate(exemplo_cnpj))
# cpf_um = CpfCnpj("15316264754")
# print(cpf_um)
documento = Documento.cria_documento(exemplo_cpf)
print(documento)
