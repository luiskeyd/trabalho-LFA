from graphviz import Digraph

def desenhar_automato(estados, estado_inicial, estados_finais, transicoes):
    dot = Digraph(format='png')

    # Estados (nós)
    for estado in estados:
        if estado == estado_inicial:
            dot.node(str(estado), shape='circle', color='green')
        elif estado in estados_finais:
            dot.node(str(estado), shape='doublecircle', color='red')
        else:
            dot.node(str(estado), shape='circle')

    # Transições (arestas)
    for (origem, simbolo), destinos in transicoes.items():
        for destino in destinos:
            dot.edge(str(origem), str(destino), label=simbolo)

    dot.render('automato')
    print("Arquivo 'automato.png' gerado!")

# Exemplo de uso:
# estados = {0, 1, 23}
# estado_inicial = 0
# estados_finais = {0, 23}
# transicoes = {
#     (0, 'a'): [23],
#     (23, 'b'): [1],
#     (1, 'b'): [0],
# }

# desenhar_automato(estados, estado_inicial, estados_finais, transicoes)
