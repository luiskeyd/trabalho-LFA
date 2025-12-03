def fecho_e(estado, transicoes):
  fecho = {estado}
  pilha = [estado]

  while pilha:
    atual = pilha.pop()

    for simbolo in ['e']:
      if (atual, simbolo) in transicoes:
        for destino in transicoes[(atual, simbolo)]:
          if destino not in fecho:
            fecho.add(destino)
            pilha.append(destino)

  return fecho

def fecho_conjunto(estados, transicoes):
  fecho = set()

  for estado in estados:
    fecho.update(fecho_e(estado, transicoes))
  
  return fecho

# Pra facilitar a nomeação dos estados de AFN pra AFD
def estados_para_strings(estados):
  return "{" + ", ".join(map(str, sorted(estados))) + "}"
