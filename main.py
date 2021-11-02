from cpf_cnpj import CpfCnpj
from validate_docbr import CNPJ

exemplo_cnpj = "26044340000108"
# cnpj = CNPJ()
# print(cnpj.validate(exemplo_cnpj))
# cpf_um = CpfCnpj("15316264754")
# print(cpf_um)
documento = CpfCnpj(exemplo_cnpj, "cnpj")
