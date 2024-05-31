import pytest
from pytest_bdd import scenarios, given, when, then
from datetime import datetime, timedelta
from app.terceiroExercicio.estacionamento import Estacionamento
from app.terceiroExercicio.ticket import Ticket

# Carrega os cenários do arquivo estacionamento.features
scenarios('C:/Users/richa/PycharmProjects/avaliacao-final-automacao-testes/app/terceiroExercicio/features/estacionamento.feature')


@pytest.fixture
def estacionamento():
    return Estacionamento()


@pytest.fixture
def ticket():
    return Ticket(placa="XYZ-1234", modelo="Carro Modelo")


@given('um veículo entra no estacionamento')
def veiculo_entra_no_estacionamento(estacionamento, ticket):
    estacionamento.emitir_ticket(ticket)


@when('o frentista emite um ticket para o veículo')
def frentista_emite_ticket(estacionamento, ticket):
    estacionamento.emitir_ticket(ticket)


@then('o ticket contém informações corretas sobre a entrada do veículo')
def ticket_contem_informacoes_corretas(ticket):
    assert ticket.placa == "XYZ-1234"
    assert ticket.modelo == "Carro Modelo"
    assert ticket.entrada is not None


@given('um veículo está estacionado há 2 horas')
def veiculo_estacionado_ha_2_horas(estacionamento, ticket):
    ticket.entrada = datetime.now() - timedelta(hours=2)
    estacionamento.emitir_ticket(ticket)


@when('o cliente apresenta o ticket de entrada para a saída')
def cliente_apresenta_ticket_para_saida(estacionamento, ticket):
    estacionamento.registrar_saida(ticket)


@then('o frentista calcula o valor devido corretamente')
def frentista_calcula_valor_devido(estacionamento, ticket):
    valor_devido = estacionamento.calcular_valor_devido(ticket)
    assert valor_devido == 20  # 15 + 5 (R$ 15 para a primeira hora, R$ 5 para a segunda hora)
