from collections import defaultdict

def ler_estados():
  print("Informe os estados do Automato (separe por virgula):")
  entrada = input().strip()
  estados = set()
  
  for item in entrada.split(","):
    estados.add(int(item.strip()))

  return estados

def ler_estado_inicial(estados):
  while True:
    print("Informe o estado inicial:")
    estado_inicial = int(input().strip())
    if estado_inicial in estados:
      print("Erro: o estado informado nao se encontra na lista de estados")

def ler_transicoes(com_epsilon=False):
  transicoes = defaultdict(list)
  print("Informe as transicoes, ex: 0a1, 1a2")

  if com_epsilon:
    print("use 'e' para transicoes epsilon")

  while True:
    entrada = input().strip()
    if not entrada:
      break

    try:
      entrada = entrada.replace(" ", "")

      if (len(entrada) < 3):
        print("Formato invalido, faz no modelo 0a1")
        continue

      origem = int(entrada[0])
      simbolo = entrada[1:-1]
      destino = int(entrada[-1])

      transicoes[(origem, simbolo)].append(destino)

    except (ValueError, IndexError):
      print("Erro ao processar '{entrada}'")

  return dict(transicoes)

def separar_alfabeto(transicoes):
  alfabeto = set()

  for (_, simbolo) in transicoes.keys():
    alfabeto.add(simbolo)

  return alfabeto

def ler_estados_finais(estados):
  print("Informe os estados finais (separe por virgula):")
  entrada = input().strip()
  estados_finais = set()

  for item in entrada.split(","):
    estado = int(item.strip())
    if estado in estados:
      estados_finais.add(estado)
    else:
      print("esse estado nao ta na lista de estados")

  return estados_finais
