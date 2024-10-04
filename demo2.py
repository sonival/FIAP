def calcular_distancia(cliente1, cliente2, distancias):
    # Retorna a distância entre dois clientes usando a matriz de distâncias
    return distancias[cliente1][cliente2]

def encontrar_cliente_mais_proximo(cliente_atual, clientes_disponiveis, distancias):
    # Encontra o cliente mais próximo do cliente atual dentre os que ainda não foram atendidos
    menor_distancia = float('inf')
    cliente_mais_proximo = None
    for cliente in clientes_disponiveis:
        distancia = calcular_distancia(cliente_atual, cliente, distancias)
        if distancia < menor_distancia:
            menor_distancia = distancia
            cliente_mais_proximo = cliente
    return cliente_mais_proximo

def vpr_algoritmo_guloso(clientes, demandas, capacidade_veiculo, distancias, janelas_de_tempo=None):
    # Inicializa as variáveis
    num_veiculos = 5  # Número de veículos disponíveis
    rotas = [[] for _ in range(num_veiculos)]
    veiculos = [{'capacidade_restante': capacidade_veiculo, 'carga_atual': 0, 'rota': [0]} for _ in range(num_veiculos)]
    clientes_nao_atendidos = clientes[:]  # Inicializa lista com todos os clientes que ainda não foram atendidos

    while clientes_nao_atendidos:
        for veiculo in veiculos:
            cliente_atual = veiculo['rota'][-1]  # Último cliente visitado (ou depósito, inicialmente)
            cliente_mais_proximo = encontrar_cliente_mais_proximo(cliente_atual, clientes_nao_atendidos, distancias)

            # Verificar capacidade do veículo e demandas do cliente
            if cliente_mais_proximo and veiculo['capacidade_restante'] >= demandas[cliente_mais_proximo]:
                veiculo['rota'].append(cliente_mais_proximo)
                veiculo['capacidade_restante'] -= demandas[cliente_mais_proximo]
                clientes_nao_atendidos.remove(cliente_mais_proximo)

            # Verifica a janela de tempo, se necessário (opcional)
            if janelas_de_tempo:
                # Verifique se o cliente pode ser atendido no intervalo de tempo correto
                pass  # Lógica de verificação da janela de tempo

            # Se o veículo não pode pegar mais clientes, ele volta ao depósito
            if veiculo['capacidade_restante'] == 0 or not clientes_nao_atendidos:
                veiculo['rota'].append(0)  # Retorna ao depósito

    # Retornar as rotas calculadas para todos os veículos
    return [veiculo['rota'] for veiculo in veiculos]

# Exemplo de execução
clientes = [1, 2, 3, 4, 5, 6]  # Clientes numerados (0 é o depósito)
demandas = {1: 10, 2: 15, 3: 20, 4: 25, 5: 30, 6: 20}  # Demanda de cada cliente
capacidade_veiculo = 50  # Capacidade de cada veículo
distancias = [
    [0, 10, 20, 30, 40, 50, 60],  # Distâncias do depósito (0) para os clientes
    [10, 0, 15, 25, 35, 45, 55],  # Distâncias entre os clientes
    [20, 15, 0, 10, 20, 30, 40],
    [30, 25, 10, 0, 15, 25, 35],
    [40, 35, 20, 15, 0, 10, 20],
    [50, 45, 30, 25, 10, 0, 15],
    [60, 55, 40, 35, 20, 15, 0]
]

rotas = vpr_algoritmo_guloso(clientes, demandas, capacidade_veiculo, distancias)
print("Rotas calculadas para os veículos:", rotas)
