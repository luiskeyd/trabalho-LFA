from automato import AFN, AFe
from entrada import (ler_estados, ler_estado_inicial, ler_transicoes, ler_estados_finais, separar_alfabeto)
from conversores import afe_para_afn, afn_para_afd
from desenho import desenhar_automato

def criar_automato(tipo):
  print(f"Criando {tipo}")

  estados = ler_estados(tipo)
  estado_inicial = ler_estado_inicial(estados)
  transicoes = ler_transicoes(tipo)
  alfabeto = separar_alfabeto(transicoes)
  estados_finais = ler_estados_finais(estados)

  if tipo == "AFe":
    return AFe(estados, alfabeto, transicoes, estado_inicial, estados_finais)
  elif tipo == "AFN":
    return AFN(estados, alfabeto, transicoes, estado_inicial, estados_finais)
  else:
    print("Informe um AFN ou um AFe pra conversão")

def main():
  while True:
    print("Digite 1 para criar um AFe e 2 para criar um AFN, 3 para sair")

    opcao = input()

    if opcao == '1':
      afe = criar_automato("AFe")
      print("AFe original")
      print(afe)

      afn = afe_para_afn(afe)
      print("AFN resultante")
      print(afn)
      desenhar_automato(afn.estados, afn.estado_inicial, afn.estados_finais, afn.transicoes)

    elif opcao == '2':
      afn = criar_automato("AFN")
      print("AFN original")
      print(afn)

      afd = afn_para_afd(afn)
      print("AFD resultante")
      print(afd)
      desenhar_automato(afd.estados, afd.estado_inicial, afd.estados_finais, afd.transicoes)

    elif opcao == '3':
      print("Vamo encerrar por aqui")
      break

    else:
      print("Invalido, tenta outra coisa")

if __name__ == "__main__":
  main()
