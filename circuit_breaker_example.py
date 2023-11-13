# Importando a classe CircuitBreaker da biblioteca resilient
from resilient import CircuitBreaker


# Função que simula a chamada ao serviço remoto
def remote_service_call():
    # Lógica para chamar o serviço remoto (simulada aqui)
    print("Chamando serviço remoto")
    # Simular uma falha para teste
    raise Exception("Erro na chamada do serviço remoto")


# Função de fallback a ser chamada em caso de falha
def fallback():
    print("Fallback acionado. Lógica de fallback aqui.")
    return "Resposta de fallback"


# Configurar o Circuit Breaker
circuit_breaker = CircuitBreaker(
    remote_service_call,  # Função principal que será protegida pelo Circuit Breaker
    fallback_function=fallback,  # Função a ser chamada em caso de falha
    failure_threshold=3,  # Limiar de falha (número máximo de falhas permitidas antes de abrir o Circuit Breaker)
    recovery_timeout=10  # Tempo de espera antes de tentar recuperar após o Circuit Breaker abrir
)

# Realizar chamadas usando o Circuit Breaker
for _ in range(5):
    try:
        # Chamar a função protegida pelo Circuit Breaker
        result = circuit_breaker.call()
        print("Resultado da chamada:", result)
    except Exception as e:
        # Capturar e tratar exceções, por exemplo, quando o Circuit Breaker está aberto
        print("Exceção capturada:", e)

    # Exibir o estado atual do Circuit Breaker após cada chamada
    print("Estado do Circuit Breaker:", circuit_breaker.state)
    print()

#Este código Python que utiliza a biblioteca resilient para implementar um Circuit Breaker,
#que ajuda a lidar com falhas em chamadas a serviços remotos,
#proporcionando uma estratégia de fallback e controlando o número de falhas permitidas antes de abrir o Circuit Breaker.