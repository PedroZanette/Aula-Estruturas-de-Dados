from datetime import datetime, timedelta

class Cliente:
    def __init__(self,nome):
        self.nome = nome
        self.protocolo = None
        self.hora_chegada = None
        self.hora_atendimento = None
        self.hora_saida = None
    
class Caixa:
    def __init__(self):
        self.fila = []
        self._prox_protocolo = 1

    def atendimento(self, duracao_segundos=5):
        if not self.fila:
            print("Fila vazia.")
            return None

        cliente = self.fila.pop(0)
        cliente.hora_atendimento = datetime.now()
        cliente.hora_saida = cliente.hora_atendimento + timedelta(seconds=duracao_segundos)
        return cliente

    def entra_na_fila(self, cliente:Cliente):
        cliente.protocolo = self._prox_protocolo
        self._prox_protocolo += 1
        cliente.hora_chegada = datetime.now()
        self.fila.append(cliente)
        print(f"{cliente.nome} entrou na fila às {cliente.hora_chegada.strftime('%H:%M:%S')}")

    def mostrar_estado(self):
        if not self.fila:
            print("Fila vazia.")
            return
        print("Fila atual:")
        for c in list(self.fila):
            print(f" - Protocolo {c.protocolo or '-'} | {c.nome}")

# ------------ Configuração ------------
nomes_clientes = [
    "Ana Silva", "Bruno Costa", "Carla Mendes", "Diego Souza", "Eduarda Lima",
    "Fernando Rocha", "Gabriela Alves", "Henrique Martins", "Isabela Duarte", "João Pedro",
    "Karen Barbosa", "Lucas Ferreira", "Mariana Gomes", "Natália Pires", "Otávio Santos",
    "Patrícia Ribeiro", "Rafael Cardoso", "Sabrina Oliveira", "Tiago Moreira", "Úrsula Andrade",
    "Vicente Teixeira", "Wesley Pinto", "Ximena Farias", "Yasmin Azevedo", "Zeca Campos",
    "Arthur Monteiro", "Bianca Tavares", "Caio Nogueira", "Daniela Furtado", "Elisa Monteiro"
]

caixa = Caixa()

intervalo_chegada = timedelta(seconds=2)
intervalo_atendimento = timedelta(seconds=10)

ultimo_cliente = datetime.now()
inicio_atendimento = None
cliente_em_atendimento = None
i = 0

# ------------ Loop ------------
while i < len(nomes_clientes) or cliente_em_atendimento:
    agora = datetime.now()

    # Entrada de clientes
    if i < len(nomes_clientes)  and agora - ultimo_cliente >= intervalo_chegada:
        novo_cliente = Cliente(nome = nomes_clientes[i])
        caixa.entra_na_fila(novo_cliente)
        ultimo_cliente = agora
        i += 1

    # Iniciar atendimento
    if not cliente_em_atendimento and caixa.fila:
        cliente_em_atendimento = caixa.atendimento()
        inicio_atendimento = agora

    # Finalizar atendimento
    if cliente_em_atendimento and agora - inicio_atendimento >= intervalo_atendimento:
        cliente_em_atendimento.hora_saida = agora
        print(f"{cliente_em_atendimento.nome} saiu às {cliente_em_atendimento.hora_saida.strftime('%H:%M:%S')}")
        cliente_em_atendimento = None