print("Informe os estados do Autômato:")
entrada = input()

lista_estados = []

for item in entrada.split(","):
    item = item.strip()
    lista_estados.append(int(item))

print("Informe o estado inicial:")
estado_inicial = int(input)

if estado_inicial not in lista_estados:
    print("O estado informado não é um estado do autômato")

lista_estados.sort()

print("Informe a função programa:")

lista_transicoes = []

while True:
    entrada = input()
    if not entrada:
        break
    lista_transicoes.append(entrada)

print("Informe os estados finais:")
entrada = input()

lista_estados_finais = []

for item in entrada.split(","):
    item = item.strip()
    lista_estados_finais.append(int(item))

lista_estados_finais.sort()