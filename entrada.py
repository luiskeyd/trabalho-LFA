from collections import defaultdict

def ler_estados(tipo):
  limites = {
    "AFe": 5,
    "AFN": 4
  }

  limite = limites[tipo]
  
  while True:
    print(f"Informe os estados do Automato (separe por virgula, no maximo {limite} estados):")
    entrada = input().strip()
    estados = set()
    
    for item in entrada.split(","):
      estados.add(int(item.strip()))

    if len(estados) > limite:
      print(f"No maximo {limite} estados")
      continue
    
    return estados


def ler_estado_inicial(estados):
  print(f"DEBUG - Estados disponiveis {estados}")
  print(f"Tipo do estado {type(estados)[0]}")
  
  while True:
    print("Informe o estado inicial:")
    estado_inicial = int(input().strip())
    
    if estado_inicial in estados:
      return estado_inicial
    
    print("Erro: o estado informado nao se encontra na lista de estados")


def ler_transicoes(tipo):
  limites = {
    "AFe": 7,
    "AFN": 8
  }

  limite = limites[tipo]

  transicoes = defaultdict(list)
  print(f"Informe as transicoes, ex: 0a1, 1a2. No maximo {limite} transicoes")

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

      if len(transicoes) > limite:
        print(f"No maximo {limite} transicoes")
        continue

    except (ValueError, IndexError):
      print("Erro ao processar '{entrada}'")

  return dict(transicoes)

def separar_alfabeto(transicoes):
  alfabeto = set()

  for (_, simbolo) in transicoes.keys():
    alfabeto.add(simbolo)

  if len(alfabeto) > 3:
    print("No maximo 3 simbolos")

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
