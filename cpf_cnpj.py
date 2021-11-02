from validate_docbr import CPF, CNPJ


class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        documento = str(documento)
        self.tipo_documeto = tipo_documento
        if self.tipo_documeto == "cpf":
            if self.cpf_e_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF é inválido!!!")
        elif self.tipo_documeto == "cnpj":
            if self.cnpj_e_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ é inválido!!!")
        else:
            raise ValueError("Documento inválido!!!")

    def __str__(self):
        if self.tipo_documeto == "cpf":
            return self.formata_cpf()
        elif self.tipo_documeto == "cnpj":
            return self.formata_cnpj()

    def cpf_e_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos inválida!!!")

    def formata_cpf(self):
        mascara = CPF()

        return mascara.mask(self.cpf)

    def formata_cnpj(self):
        mascara = CNPJ()

        return mascara.mask(self.cnpj)

    def cnpj_e_valido(self, cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de digitos inválida!!!")
