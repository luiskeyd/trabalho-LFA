class Automato:
  def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
    self.estados = estados
    self.alfabeto = alfabeto
    self.transicoes = transicoes
    self.estado_inicial = estado_inicial
    self.estados_finais = estados_finais

    def __str__(self):
      return f"""
        Autômato:
        - Estados: {sorted(self.estados)}
        - Alfabeto: {sorted(self.alfabeto)}
        - Estado Inicial: {self.estado_inicial}
        - Estados Finais: {sorted(self.estados_finais)}
        - Transições: {dict(self.transcoes)}
      """
    

class AFN(Automato):
  pass

class AFe(Automato):
  pass

class AFD(Automato):
  pass
