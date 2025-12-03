from collections import defaultdict
from automato import AFN, AFD, AFe
from utils import fecho, fecho_conjunto, estados_para_strings

def afe_para_afn(afe):
  print("Convertendo aqui")

  novas_transicoes = defaultdict(list)

  for estado in afe.estados:
    fecho = fecho(estado, afe.transicoes)

    for simbolo in afe.alfabeto:
      if simbolo in ['e']:
        continue

      destinos = set()

      # Função programa
      for estado_fecho in fecho:
        if (estado_fecho, simbolo) in afe.transicoes:
          for destino in afe.transicoes[(estado_fecho, simbolo)]:
            destinos.update(fecho(destino, afe.transicoes))

      if destinos:
        novas_transicoes[(estado, simbolo)] = list(destinos)

  novos_finais = set()
  for estado in afe.estados:
    fecho = fecho(estado, afe.transicoes)
    if (fecho & afe.estados_finais):
      novos_finais.add(estado)

  novo_alfabeto = set()
  for s in afe.alfabeto:
    if s not in ['e']:
      novo_alfabeto.add(s)

  return AFN(
    afe.estados,
    novo_alfabeto,
    dict(novas_transicoes),
    afe.estado_inicial,
    novos_finais
  )

def afn_para_afd(afn):
  print("Convertendo aqui")

  estado_inicial_afd = frozenset([afn.estado_inicial])

  estados_afd = set()
  transicoes_afd = {}
  estados_finais_afd = set()

  fila = [estado_inicial_afd]
  processados = set()

  while fila:
    estado_atual = fila.pop(0)

    if estado_atual in processados:
      continue

    processados.add(estado_atual)
    estados_afd.add(estado_atual)

    encontra_final = False
    for estado in estado_atual:
      if estado in afn.estados_finais:
        encontra_final = True
        break

    if encontra_final:
      estados_finais_afd.add(estado_atual)

    for simbolo in afn.alfabeto:
      destinos = set()

      for estado in estado_atual:
        if (estado, simbolo) in afn.transicoes:
          destinos.update(afn.transicoes[(estado, simbolo)])

        if destinos:
          novo_estado = frozenset(destinos)
          transicoes_afd[(estado_atual, simbolo)] = novo_estado

          if novo_estado not in processados:
            fila.append(novo_estado)

  return AFD(
    estados_afd,
    afn.alfabeto,
    transicoes_afd,
    estado_inicial_afd,
    estados_finais_afd
  )
