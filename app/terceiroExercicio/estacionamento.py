from datetime import datetime


class Estacionamento:
    def __init__(self):
        self.tickets_em_aberto = []

    def emitir_ticket(self, ticket):
        self.tickets_em_aberto.append(ticket)

    def registrar_saida(self, ticket):
        ticket.saida = datetime.now()

    def calcular_valor_devido(self, ticket):
        if ticket.entrada is None or ticket.saida is None:
            raise ValueError("Ticket inválido: entrada ou saída não registrada.")

        tempo_decorrido = ticket.saida - ticket.entrada
        horas_decorridas = tempo_decorrido.total_seconds() / 3600  # Converter para horas
        valor_devido = 15 + max(0, horas_decorridas - 1) * 5  # R$ 15 para a primeira hora, RS 5 para as demais

        return valor_devido
