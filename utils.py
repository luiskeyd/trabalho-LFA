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

def formatar_estados(e):
  if isinstance(e, frozenset):
    itens = sorted(list(e))

    texto = ''
    for i in range(len(itens)):
      texto += str(itens[i])

    return texto
  
  return str(e)

def converter_estados(estados, estado_inicial, estados_finais, transicoes):
  if isinstance(estado_inicial, frozenset):
    estado_inicial_convertido = formatar_estados(estado_inicial)
  else:
    estado_inicial_convertido = str(estado_inicial)
  

  estados_convertidos = []
  for e in estados:
    estados_convertidos.append(int(formatar_estados(e)))
  
  estados_convertidos = set(sorted(estados_convertidos))


  finais_convertidos = []
  for e in estados_finais:
    finais_convertidos.append(int(formatar_estados(e)))

  finais_convertidos = set(sorted(finais_convertidos))

  transicoes_convertidas = {}
  for chave, destino in transicoes.items():
    origem, simbolo = chave

    origem_formatado = formatar_estados(origem)

    if isinstance(destino, list):
      destino_formatado = []

      for d in destino:
        destino_formatado.append(formatar_estados(d))

    else:
      destino_formatado = formatar_estados(destino)

    transicoes_convertidas[(origem_formatado, simbolo)] = destino_formatado

  transicoes_formatadas = {}
  for (origem, simbolo), destino in transicoes_convertidas.items():
    if not isinstance(destino, list):
      destino = [int(destino)]
    transicoes_formatadas[(int(origem), simbolo)] = destino

  return estados_convertidos, estado_inicial_convertido, finais_convertidos, transicoes_formatadas
