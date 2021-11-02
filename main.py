from cpf_cnpj import CpfCnpj
from validate_docbr import CNPJ

exemplo_cnpj = "26044340000108"
exemplo_cpf = "76567524049"
# cnpj = CNPJ()
# print(cnpj.validate(exemplo_cnpj))
# cpf_um = CpfCnpj("15316264754")
# print(cpf_um)
documento = CpfCnpj(exemplo_cpf, "cpf")
print(documento)
