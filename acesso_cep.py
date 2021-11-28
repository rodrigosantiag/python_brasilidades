import requests

class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)

        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!!!")

    def __str__(self):
        return self.format_cep()

    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def format_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"

    def acessa_via_cep(self):
        url = f"http://viacep.com.br/ws/{self.cep}/json"

        response = requests.get(url)
        result = response.json()

        return (
            result.get("bairro"),
            result.get("localidade"),
            result.get("uf")
        )
