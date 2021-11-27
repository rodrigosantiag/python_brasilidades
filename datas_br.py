from datetime import datetime


class DatasBR:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro",
            "fevereiro",
            "março",
            "abril",
            "maio",
            "junho",
            "julho",
            "agosto",
            "setembro",
            "outubro",
            "novembro",
            "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month - 1

        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dias_semana = [
            "segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"
        ]

        dia_semana = self.momento_cadastro.weekday()

        return dias_semana[dia_semana]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")

        return data_formatada
