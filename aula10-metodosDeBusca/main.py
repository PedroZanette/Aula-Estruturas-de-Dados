from datetime import datetime


class TimeElapsed:

    def __init__(self):
        self.start_time = datetime.now()
        self.elapsed_time = None

    def finish(self):
        self.elapsed_time = (datetime.now() - self.start_time)


def get_sorted_list(amount):
    return [i for i in range(amount)]


def busca_linear(lista, elemento, achou_linear = False):

    for i in range(len(lista)):
        if elemento == lista[i]:
            achou_linear = True
            return achou_linear
    return achou_linear    

def busca_binaria(lista, elemento, inicio = 0, achou_binario = False):
    
    fim = len(lista) - 1

    while inicio <= fim :
        meio = (inicio + fim) // 2
        valor_meio = lista[meio]

        if valor_meio == elemento:
            achou_binario = True
            return achou_binario
        else:
            if valor_meio < elemento:
                inicio = meio + 1
            else:
                fim = meio - 1

    return achou_binario


lista = get_sorted_list(1000000)

elemento_procurado = int(input("\nDigite o número que queres achar: "))

# ---- Busca Linear ----
tempo_linear = TimeElapsed()
resultado_linear = busca_linear(lista, elemento_procurado)
tempo_linear.finish()

# ---- Busca Binária ----
tempo_binaria = TimeElapsed()
resultado_binaria = busca_binaria(lista, elemento_procurado)
tempo_binaria.finish()

# ---- Busca Hash ----
tempo_hash = TimeElapsed()
resultado_hash = lista[elemento_procurado]
tempo_hash.finish()

# ---- Resultados ----
print("\n=== RESULTADOS ===")
print(f"Elemento procurado: {elemento_procurado} ms")
print(f"Busca Hash -> Tempo: {tempo_hash.elapsed_time.microseconds}")
print(f"Busca Linear  -> Achou: {resultado_linear}, Tempo: {tempo_linear.elapsed_time.microseconds} ms")
print(f"Busca Binária -> Achou: {resultado_binaria}, Tempo: {tempo_binaria.elapsed_time.microseconds} ms")

# ---- Complexidade ----
print("\n=== ANÁLISE TEÓRICA ===")
print("Busca Linear  -> Complexidade: O(n) — percorre a lista inteira.")
print("Busca Binária -> Complexidade: O(log n) — divide a lista pela metade a cada passo.")
