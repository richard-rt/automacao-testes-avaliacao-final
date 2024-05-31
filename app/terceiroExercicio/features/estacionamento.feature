# arquivo: estacionamento.feature

Feature: Controle de estacionamento

    Scenario: Emitir um ticket para entrada de veículo
        Given um veículo entra no estacionamento
        When o frentista emite um ticket para o veículo
        Then o ticket contém informações corretas sobre a entrada do veículo

    Scenario: calcula o valor devido para saída de veículo
        Given um veículo está estacionado há 2 horas
        When o cliente apresenta o ticket de entrada para a saída
        Then o frentista calcula o valor devido corretamente